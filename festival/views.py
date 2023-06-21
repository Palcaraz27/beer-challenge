import json
import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from result import Err

from app.cqrs.dispatcher import command_bus, query_bus
from core.festival.application.command import CreateBeerCommand, RemoveBeerCommand, CreateDispenserCommand
from core.festival.application.query import GetBeerByIdQuery, GetBeersQuery
from festival.serializers import RequestBeerSerializer, RequestDispenserSerializer


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

        logger.info("Successful beers request.")
        return Response({"success": True, "beers": [store.to_json() for store in response.ok()]}, status=status.HTTP_200_OK)

    def delete(self, request) -> Response:
        body = json.loads(request.body)
        beer_id = body.get("id", "")
        response = command_bus.dispatch(RemoveBeerCommand(id=beer_id))

        if isinstance(response, Err):
            logger.warning("Error removing beers: {error}".format(error=response.err().message))
            return Response(response.err().message, status=status.HTTP_400_BAD_REQUEST)

        logger.info("Beer removed: {id}".format(id=beer_id))
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)

class BeerByIdView(APIView):
    def get(self, request, id) -> Response:
        response = query_bus.dispatch(GetBeerByIdQuery(id=id))

        if isinstance(response, Err):
            logger.warning("Error getting beer by id: {error}".format(error=response.err().message))
            return Response(response.err().message, status=status.HTTP_400_BAD_REQUEST)

        if response.ok() == None:
            logger.info("Successful beer by id request but it not found.")
            Response({"success": True, "beer": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        logger.info("Successful beer by id request.")
        return Response({"success": True, "beer": response.ok().to_json()}, status=status.HTTP_200_OK)


class DispenserView(APIView):
    @swagger_auto_schema(request_body=RequestDispenserSerializer)
    def post(self, request) -> Response:
        body = json.loads(request.body)

        response = command_bus.dispatch(CreateDispenserCommand(
            beer_id=body.get("beer_id", ""),
            flow_volume=body.get("flow_volume", 0),
            )
        )

        if isinstance(response, Err):
            logger.warning("Error creating dispenser: {error}".format(error=response.err().message))
            return Response(response.err().message, status=status.HTTP_400_BAD_REQUEST)

        logger.info("Dispenser created")
        return Response({"success": True}, status=status.HTTP_201_CREATED)
