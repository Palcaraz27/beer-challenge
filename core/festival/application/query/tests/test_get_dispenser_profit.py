import pytest
from result import Ok

from core.festival.application.query import GetDispenserProfitInfoQuery, GetDispenserProfitInfoQueryHandler
from core.festival.infrastructure.services.inmemory_beer_repository import InMemoryBeerRepository
from core.festival.infrastructure.services.inmemory_dispenser_repository import InMemoryDispenserRepository
from core.festival.tests.beer_builder import BeerBuilder
from core.festival.tests.dispenser_builder import DispenserBuilder


@pytest.mark.asyncio
async def test_get_dispenser_profit_success() -> None:
    # Arrange
    beer = BeerBuilder().build()
    beer_repository = InMemoryBeerRepository(beers=[beer])
    dispenser = DispenserBuilder().build_with_beer(beer.beer_id.value)
    dispenser_repository = InMemoryDispenserRepository(dispensers=[dispenser])
    handler = GetDispenserProfitInfoQueryHandler(dispenser_repository, beer_repository)
    query = GetDispenserProfitInfoQuery(id=dispenser.dispenser_id.value)

    # Act
    result = await handler.handle(query)

    # Assert
    assert isinstance(result, Ok)
