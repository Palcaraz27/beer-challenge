from typing import Dict

from app.cqrs.models import Command, CommandHandler, Query, QueryHandler
from core.festival.application.command import (
    CloseDispenserCommand,
    CloseDispenserCommandHandler,
    CreateDispenserCommand,
    CreateDispenserCommandHandler,
    OpenDispenserCommand,
    OpenDispenserCommandHandler,
)
from core.festival.application.query import (
    GetDispensersQuery,
    GetDispensersQueryHandler,
    GetDispenserByIdQuery,
    GetDispenserByIdQueryHandler,
    GetDispenserProfitInfoQuery,
    GetDispenserProfitInfoQueryHandler
)
from core.festival.infrastructure.services.django_beer_repository import DjangoBeerRepository
from core.festival.infrastructure.services.django_dispenser_repository import DjangoDispenserRepository


django_dispenser_repository = DjangoDispenserRepository()
django_beer_repository = DjangoBeerRepository()

command_handlers: Dict[Command, CommandHandler] = {
    CloseDispenserCommand: CloseDispenserCommandHandler(
        dispenser_repository=django_dispenser_repository
    ),
    CreateDispenserCommand: CreateDispenserCommandHandler(
        dispenser_repository=django_dispenser_repository
    ),
    OpenDispenserCommand: OpenDispenserCommandHandler(
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
    GetDispenserProfitInfoQuery: GetDispenserProfitInfoQueryHandler(
        dispenser_repository=django_dispenser_repository, beer_repository=django_beer_repository
    ),
}
