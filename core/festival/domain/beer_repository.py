from typing_extensions import Protocol

from .beer import Beer


class BeerRepository(Protocol):
    async def save(self, beer: Beer) -> None:
        raise NotImplementedError
