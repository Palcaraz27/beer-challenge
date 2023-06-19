import pytest
from result import Ok

from core.festival.application.query.get_beers_query import GetBeersQuery
from core.festival.application.query.get_beers_query_handler import GetBeersQueryHandler
from core.festival.infrastructure.services.inmemory_beer_repository import InMemoryBeerRepository
from core.festival.tests.beer_builder import BeerBuilder


@pytest.mark.asyncio
async def test_get_all_beers_success() -> None:
    # Arrange
    beer = BeerBuilder().build()
    beer_repository = InMemoryBeerRepository(beers=[beer])
    handler = GetBeersQueryHandler(beer_repository)
    query = GetBeersQuery()

    # Act
    result = await handler.handle(query)

    # Assert
    assert isinstance(result, Ok)