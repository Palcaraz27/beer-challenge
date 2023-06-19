from typing import Dict

from core.festival.application.command import (
    CreateBeerCommand,
    CreateBeerCommandHandler,
    RemoveBeerCommand,
    RemoveBeerCommandHandler
)
from core.festival.application.query import (
    GetBeersQuery,
    GetBeersQueryHandler,
    GetBeerByIdQuery,
    GetBeerByIdQueryHandler
)
from core.festival.infrastructure.services.django_beer_repository import DjangoBeerRepository
from app.cqrs.models import Command, CommandHandler, Query, QueryHandler


django_beer_repository = DjangoBeerRepository()

command_handlers: Dict[Command, CommandHandler] = {
    CreateBeerCommand: CreateBeerCommandHandler(
        beer_repository=django_beer_repository
    ),
    RemoveBeerCommand: RemoveBeerCommandHandler(
        beer_repository=django_beer_repository
    ),
}

query_handlers: Dict[Query, QueryHandler] = {
    GetBeersQuery: GetBeersQueryHandler(
        beer_repository=django_beer_repository
    ),
    GetBeerByIdQuery: GetBeerByIdQueryHandler(
        beer_repository=django_beer_repository
    ),
}
