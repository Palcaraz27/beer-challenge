from typing import List
from result import Ok, Result

from app.cqrs.models import QueryHandler
from core.festival.application.query.get_beers_query import GetBeersQuery
from core.festival.domain.beer_repository import BeerRepository
from core.festival.domain.errors import BeerError
from festival.models import Beer


class GetBeersQueryHandler(QueryHandler[GetBeersQuery]):
    def __init__(self, beer_repository: BeerRepository) -> None:
        self._beer_repository = beer_repository

    async def handle(self, query: GetBeersQuery) -> Result[List[Beer], BeerError]:

        beers = await self._beer_repository.get_all()
        
        return Ok(beers)
