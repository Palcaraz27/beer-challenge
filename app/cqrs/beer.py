from typing import Dict
from core.festival.application.command.create_beer_command import CreateBeerCommand
from core.festival.application.command.create_beer_command_handler import CreateBeerCommandHandler
from core.festival.infrastructure.services.django_beer_repository import DjangoBeerRepository

from app.cqrs.models import Command, CommandHandler


django_beer_repository = DjangoBeerRepository()

command_handlers: Dict[Command, CommandHandler] = {
    CreateBeerCommand: CreateBeerCommandHandler(
        beer_repository=django_beer_repository
    ),
}
