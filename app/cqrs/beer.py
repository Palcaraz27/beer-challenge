from typing import Dict

from core.festival.application.command.create_beer_command import CreateBeerCommand
from core.festival.application.command.create_beer_command_handler import CreateBeerCommandHandler
from core.festival.application.query.get_beer_by_id_query import GetBeerByIdQuery
from core.festival.application.query.get_beer_by_id_query_handler import GetBeerByIdQueryHandler
from core.festival.application.query.get_beers_query import GetBeersQuery
from core.festival.application.query.get_beers_query_handler import GetBeersQueryHandler
from core.festival.infrastructure.services.django_beer_repository import DjangoBeerRepository
from app.cqrs.models import Command, CommandHandler, Query, QueryHandler


django_beer_repository = DjangoBeerRepository()

command_handlers: Dict[Command, CommandHandler] = {
    CreateBeerCommand: CreateBeerCommandHandler(
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
