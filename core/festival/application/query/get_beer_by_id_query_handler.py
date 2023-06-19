from typing import Optional
from result import Ok, Result

from app.cqrs.models import QueryHandler
from core.festival.application.query.get_beer_by_id_query import GetBeerByIdQuery
from core.festival.domain.beer import BeerId
from core.festival.domain.beer_repository import BeerRepository
from core.festival.domain.errors import BeerError
from festival.models import Beer


class GetBeerByIdQueryHandler(QueryHandler[GetBeerByIdQuery]):
    def __init__(self, beer_repository: BeerRepository) -> None:
        self._beer_repository = beer_repository

    async def handle(self, query: GetBeerByIdQuery) -> Result[Optional[Beer], BeerError]:

        beer = await self._beer_repository.get_by_id(BeerId(query.id))
        
        return Ok(beer)
