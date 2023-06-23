import pytest
from result import Ok

from core.festival.application.query import GetDispensersQuery, GetDispensersQueryHandler
from core.festival.infrastructure.services.inmemory_dispenser_repository import InMemoryDispenserRepository
from core.festival.tests.dispenser_builder import DispenserBuilder


@pytest.mark.asyncio
async def test_get_all_dispensers_success() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    beer_repository = InMemoryDispenserRepository(dispensers=[dispenser])
    handler = GetDispensersQueryHandler(beer_repository)
    query = GetDispensersQuery()

    # Act
    result = await handler.handle(query)

    # Assert
    assert isinstance(result, Ok)
