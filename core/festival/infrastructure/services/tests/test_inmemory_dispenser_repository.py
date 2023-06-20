import uuid
import pytest

from core.festival.tests.dispenser_builder import DispenserBuilder
from ..inmemory_dispenser_repository import InMemoryDispenserRepository


@pytest.mark.asyncio
async def test_save_new_dipenser() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    repository = InMemoryDispenserRepository(dipensers=[])

    # Act
    await repository.save(dispenser)

    # Assert
    dispenser_found = await repository.get_by_id(dispenser_id=dispenser.dispenser_id)
    assert dispenser_found
    assert dispenser_found.dispenser_id == dispenser.dispenser_id

@pytest.mark.asyncio
async def test_get_all_dispensers() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    repository = InMemoryDispenserRepository(dipensers=[dispenser])

    # Act
    result = await repository.get_all()

    # Assert
    assert result
    assert result[0] == dispenser

@pytest.mark.asyncio
async def test_get_by_id_dispenser_success() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    repository = InMemoryDispenserRepository(dipensers=[dispenser])

    # Act
    result = await repository.get_by_id(dispenser_id=dispenser.dispenser_id)

    # Assert
    assert result
    assert result == dispenser

@pytest.mark.asyncio
async def test_get_by_id_dispenser_not_found() -> None:
    # Arrange
    repository = InMemoryDispenserRepository(dipensers=[])

    # Act
    result = await repository.get_by_id(dispenser_id=uuid.uuid4())

    # Assert
    assert result == None

@pytest.mark.asyncio
async def test_remove_dispenser_success() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    repository = InMemoryDispenserRepository(dipensers=[dispenser])

    # Act
    await repository.delete(dispenser)

    # Assert
    assert len(repository._dispensers) == 0

@pytest.mark.asyncio
async def test_remove_dispenser_not_found() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    dispenser_to_remove = DispenserBuilder().build()
    repository = InMemoryDispenserRepository(dipensers=[dispenser])

    # Act
    await repository.delete(dispenser_to_remove)

    # Assert
    assert len(repository._dispensers) == 1

