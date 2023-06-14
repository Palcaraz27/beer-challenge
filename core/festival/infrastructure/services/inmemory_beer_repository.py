from typing import List
from core.festival.domain.beer import Beer
from core.festival.domain.beer_repository import BeerRepository


class InMemoryBeerRepository(BeerRepository):
    def __init__(self, beers: List[Beer]) -> None:
        self._beers = beers or []

    async def save(self, beer: Beer) -> None:
        beer_found = next(filter(lambda s: beer.beer_id == s.beer_id, self._beers), None)

        if beer_found is None:
            self._beers.append(beer)
        