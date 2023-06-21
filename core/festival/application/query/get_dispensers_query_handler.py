from typing import List
from result import Ok, Result

from app.cqrs.models import QueryHandler
from core.festival.application.query.get_dispensers_query import GetDispensersQuery
from core.festival.domain.dispenser_repository import DispenserRepository
from core.festival.domain.errors import DispenserError
from festival.models import Dispenser


class GetDispensersQueryHandler(QueryHandler[GetDispensersQuery]):
    def __init__(self, dispenser_repository: DispenserRepository) -> None:
        self._dispenser_repository = dispenser_repository

    async def handle(self, query: GetDispensersQuery) -> Result[List[Dispenser], DispenserError]:
        dipensers = await self._dispenser_repository.get_all()

        return Ok(dipensers)
