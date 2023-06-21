from typing import Optional
from result import Ok, Result

from app.cqrs.models import QueryHandler
from core.festival.application.query.get_dispenser_by_id_query import GetDispenserByIdQuery
from core.festival.domain.dispenser import DispenserId
from core.festival.domain.dispenser_repository import DispenserRepository
from core.festival.domain.errors import DispenserError
from festival.models import Dispenser


class GetDispenserByIdQueryHandler(QueryHandler[GetDispenserByIdQuery]):
    def __init__(self, dispenser_repository: DispenserRepository) -> None:
        self._dispenser_repository = dispenser_repository

    async def handle(self, query: GetDispenserByIdQuery) -> Result[Optional[Dispenser], DispenserError]:

        dispenser = await self._dispenser_repository.get_by_id(DispenserId(query.id))
        
        return Ok(dispenser)

