import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from result import Err

from app.cqrs.dispatcher import command_bus
from core.festival.application.command.create_beer_command import CreateBeerCommand

class BeerView(APIView):
    def post(self, request) -> Response:
        body = json.loads(request.body)

        response = command_bus.dispatch(CreateBeerCommand(
            name=body.get("name", ""),
            price=body.get("price", 0),
            )
        )

        if isinstance(response, Err):
            # add logger warning
            return Response(response.err().message, status=status.HTTP_400_BAD_REQUEST)

        # add logger info
        return Response({"success": True}, status=status.HTTP_201_CREATED)
