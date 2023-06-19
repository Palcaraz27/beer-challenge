from typing import List, Optional
from core.festival.domain.beer import Beer, BeerId
from core.festival.domain.beer_repository import BeerRepository


class InMemoryBeerRepository(BeerRepository):
    def __init__(self, beers: List[Beer]) -> None:
        self._beers = beers or []

    async def save(self, beer: Beer) -> None:
        beer_found = next(filter(lambda s: beer.beer_id == s.beer_id, self._beers), None)

        if beer_found is None:
            self._beers.append(beer)

    async def get_by_id(self, beer_id: BeerId) -> Optional[Beer]:
        beer_found = next(
            filter(lambda beer: beer_id == beer.beer_id, self._beers), None
        )

        return beer_found

    async def get_all(self) -> List[Beer]:
        return self._beers

    async def delete(self, beer: Beer) -> None:
        if beer in self._beers:
            self._beers.remove(beer)
