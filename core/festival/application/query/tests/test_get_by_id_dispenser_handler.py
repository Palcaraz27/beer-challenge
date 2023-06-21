import pytest
from result import Ok

from core.festival.application.query import GetDispenserByIdQuery, GetDispenserByIdQueryHandler
from core.festival.infrastructure.services.inmemory_dispenser_repository import InMemoryDispenserRepository
from core.festival.tests.dispenser_builder import DispenserBuilder


@pytest.mark.asyncio
async def test_get_dispenser_by_id_success() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    dispenser_repository = InMemoryDispenserRepository(dipensers=[dispenser])
    handler = GetDispenserByIdQueryHandler(dispenser_repository)
    query = GetDispenserByIdQuery(id=dispenser.dispenser_id.value)

    # Act
    result = await handler.handle(query)

    # Assert
    assert isinstance(result, Ok)
    assert result.ok() == dispenser
