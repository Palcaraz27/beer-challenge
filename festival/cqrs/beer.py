from typing import Any, Dict, Type
from core.festival.application.command.create_beer_command import CreateBeerCommand
from core.festival.application.command.create_beer_command_handler import CreateBeerCommandHandler
from core.festival.infrastructure.services.django_beer_repository import DjangoBeerRepository

from festival.cqrs.models import Command, CommandHandler


django_beer_repository = DjangoBeerRepository()

command_handlers: Dict[Type[Command[Any]], CommandHandler[Any]] = {
    CreateBeerCommand: CreateBeerCommandHandler(
        beer_repository=django_beer_repository
    ),
}
