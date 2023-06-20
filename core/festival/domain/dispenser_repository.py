from typing import List, Optional
from typing_extensions import Protocol

from .dispenser import Dispenser, DispenserId


class DispenserRepository(Protocol):
    async def save(self, dispenser: Dispenser) -> None:
        raise NotImplementedError

    async def get_by_id(self, dispenser_id: DispenserId) -> Optional[Dispenser]:
        raise NotImplementedError

    async def get_all(self) -> List[Dispenser]:
        raise NotImplementedError

    async def delete(self, dispenser: Dispenser) -> None:
        raise NotImplementedError
