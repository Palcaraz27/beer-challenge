from typing import List, Optional
from typing_extensions import Protocol

from .beer import Beer, BeerId


class BeerRepository(Protocol):
    async def save(self, beer: Beer) -> None:
        raise NotImplementedError

    async def get_by_id(self, beer_id: BeerId) -> Optional[Beer]:
        raise NotImplementedError

    async def get_all(self) -> List[Beer]:
        raise NotImplementedError
