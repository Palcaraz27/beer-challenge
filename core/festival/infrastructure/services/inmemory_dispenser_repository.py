from typing import List, Optional

from core.festival.domain.dispenser import Dispenser, DispenserId
from core.festival.domain.dispenser_repository import DispenserRepository


class InMemoryDispenserRepository(DispenserRepository):
    def __init__(self, dipensers: List[Dispenser]) -> None:
        self._dispensers = dipensers or []

    async def save(self, dispenser: Dispenser) -> None:
        dispenser_found = next(filter(lambda s: dispenser.dispenser_id == s.dispenser_id, self._dispensers), None)

        if dispenser_found is None:
            self._dispensers.append(dispenser)

    async def get_by_id(self, dispenser_id: DispenserId) -> Optional[Dispenser]:
        dispenser_found = next(
            filter(lambda dispenser: dispenser_id == dispenser.dispenser_id, self._dispensers), None
        )

        return dispenser_found

    async def get_all(self) -> List[Dispenser]:
        return self._dispensers

    async def delete(self, dispenser: Dispenser) -> None:
        if dispenser in self._dispensers:
            self._dispensers.remove(dispenser)
