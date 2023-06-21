from typing import Dict

from app.cqrs.models import Command, CommandHandler, Query, QueryHandler
from core.festival.application.command import CreateDispenserCommand, CreateDispenserCommandHandler
from core.festival.application.query import (
    GetDispensersQuery,
    GetDispensersQueryHandler,
    GetDispenserByIdQuery,
    GetDispenserByIdQueryHandler)
from core.festival.infrastructure.services.django_dispenser_repository import DjangoDispenserRepository


django_dispenser_repository = DjangoDispenserRepository()

command_handlers: Dict[Command, CommandHandler] = {
    CreateDispenserCommand: CreateDispenserCommandHandler(
        dispenser_repository=django_dispenser_repository
    ),
}

query_handlers: Dict[Query, QueryHandler] = {
    GetDispensersQuery: GetDispensersQueryHandler(
        dispenser_repository=django_dispenser_repository
    ),
    GetDispenserByIdQuery: GetDispenserByIdQueryHandler(
        dispenser_repository=django_dispenser_repository
    ),
}
