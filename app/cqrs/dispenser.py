from typing import Dict

from app.cqrs.models import Command, CommandHandler
from core.festival.application.command import CreateDispenserCommand, CreateDispenserCommandHandler
from core.festival.infrastructure.services.django_dispenser_repository import DjangoDispenserRepository


django_dispenser_repository = DjangoDispenserRepository()

command_handlers: Dict[Command, CommandHandler] = {
    CreateDispenserCommand: CreateDispenserCommandHandler(
        dispenser_repository=django_dispenser_repository
    ),
}
