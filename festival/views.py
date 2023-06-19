import json
import logging

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from result import Err

from app.cqrs.dispatcher import command_bus
from core.festival.application.command.create_beer_command import CreateBeerCommand


logger = logging.getLogger(__name__)


class BeerView(APIView):
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
