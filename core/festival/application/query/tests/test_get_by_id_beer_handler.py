import uuid
import pytest
from result import Ok

from core.festival.application.query.get_beer_by_id_query import GetBeerByIdQuery
from core.festival.application.query.get_beer_by_id_query_handler import GetBeerByIdQueryHandler
from core.festival.infrastructure.services.inmemory_beer_repository import InMemoryBeerRepository
from core.festival.tests.beer_builder import BeerBuilder



@pytest.mark.asyncio
async def test_get_beer_by_id_success() -> None:
    # Arrange
    beer = BeerBuilder().build()
    beer_repository = InMemoryBeerRepository(beers=[beer])
    handler = GetBeerByIdQueryHandler(beer_repository)
    query = GetBeerByIdQuery(id=beer.beer_id)

    # Act
    result = await handler.handle(query)

    # Assert
    assert isinstance(result, Ok)
    assert result.ok() == beer

@pytest.mark.asyncio
async def test_get_beer_by_id_not_found() -> None:
    # Arrange
    beer_repository = InMemoryBeerRepository(beers=[])
    handler = GetBeerByIdQueryHandler(beer_repository)
    query = GetBeerByIdQuery(id=uuid.uuid4())

    # Act
    result = await handler.handle(query)

    # Assert
    assert isinstance(result, Ok)
    assert result.ok() == None
