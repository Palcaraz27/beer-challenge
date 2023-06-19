import json
import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from result import Err

from app.cqrs.dispatcher import command_bus, query_bus
from core.festival.application.command.create_beer_command import CreateBeerCommand
from core.festival.application.query.get_beers_query import GetBeersQuery
from festival.serializers import RequestBeerSerializer


logger = logging.getLogger(__name__)


class BeerView(APIView):
    @swagger_auto_schema(request_body=RequestBeerSerializer)
    def post(self, request) -> Response:
        body = json.loads(request.body)

        response = command_bus.dispatch(CreateBeerCommand(
            name=body.get("name", ""),
            price=body.get("price", 0),
            )
        )

        if isinstance(response, Err):
            logger.warning("Error creating beer: {error}".format(error=response.err().message))
            return Response(response.err().message, status=status.HTTP_400_BAD_REQUEST)

        logger.info("Beer created: {name}".format(name=body.get("name")))
        return Response({"success": True}, status=status.HTTP_201_CREATED)

    def get(self, request) -> Response:
        response = query_bus.dispatch(GetBeersQuery())

        if isinstance(response, Err):
            logger.warning("Error getting beers: {error}".format(error=response.err().message))
            return Response(response.err().message, status=status.HTTP_400_BAD_REQUEST)

        logger.info("Successful beer request.")
        return Response({"success": True, "beers": [store.to_json() for store in response.ok()]}, status=status.HTTP_200_OK)
