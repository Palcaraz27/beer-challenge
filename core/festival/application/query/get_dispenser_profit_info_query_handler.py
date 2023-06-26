from typing import Optional
from result import Ok, Result
from app.cqrs.models import QueryHandler
from core.festival.application.dto.dispenser import DispenserProfitDTO
from core.festival.application.query.get_dispenser_profit_info_query import GetDispenserProfitInfoQuery
from core.festival.domain.beer import BeerId
from core.festival.domain.beer_repository import BeerRepository
from core.festival.domain.dispenser import DispenserId
from core.festival.domain.dispenser_repository import DispenserRepository
from core.festival.domain.errors import DispenserError


class GetDispenserProfitInfoQueryHandler(QueryHandler[GetDispenserProfitInfoQuery]):
    def __init__(self, dispenser_repository: DispenserRepository, beer_repository: BeerRepository) -> None:
        self._beer_repository = beer_repository
        self._dispenser_repository = dispenser_repository

    async def handle(self, query: GetDispenserProfitInfoQuery) -> Result[Optional[DispenserProfitDTO], DispenserError]:

        dispenser = await self._dispenser_repository.get_by_id(DispenserId(query.id))
        beer = await self._beer_repository.get_by_id(BeerId(dispenser.beer_id.value))
        
        return Ok(DispenserProfitDTO(dispenser, beer.price))
