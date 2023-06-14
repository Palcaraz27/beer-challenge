import pytest

from core.festival.tests.beer_builder import BeerBuilder
from ..inmemory_beer_repository import InMemoryBeerRepository


@pytest.mark.asyncio
async def test_save_new_beer() -> None:
    # Arrange
    beer = BeerBuilder().build()
    repository = InMemoryBeerRepository(beers=[])

    # Act
    await repository.save(beer)

    # Assert
    beer_found = await repository.get_by_id(beer_id=beer.beer_id)
    assert beer_found
    assert beer_found.beer_id == beer.beer_id
