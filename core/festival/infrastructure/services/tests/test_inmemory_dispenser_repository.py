import uuid
import pytest

from core.festival.tests.dispenser_builder import DispenserBuilder
from ..inmemory_dispenser_repository import InMemoryDispenserRepository


@pytest.mark.asyncio
async def test_save_new_dipenser() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    repository = InMemoryDispenserRepository(dispensers=[])

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
    repository = InMemoryDispenserRepository(dispensers=[dispenser])

    # Act
    result = await repository.get_all()

    # Assert
    assert result
    assert result[0] == dispenser

@pytest.mark.asyncio
async def test_get_by_id_dispenser_success() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    repository = InMemoryDispenserRepository(dispensers=[dispenser])

    # Act
    result = await repository.get_by_id(dispenser_id=dispenser.dispenser_id)

    # Assert
    assert result
    assert result == dispenser

@pytest.mark.asyncio
async def test_get_by_id_dispenser_not_found() -> None:
    # Arrange
    repository = InMemoryDispenserRepository(dispensers=[])

    # Act
    result = await repository.get_by_id(dispenser_id=uuid.uuid4())

    # Assert
    assert result == None

@pytest.mark.asyncio
async def test_remove_dispenser_success() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    repository = InMemoryDispenserRepository(dispensers=[dispenser])

    # Act
    await repository.delete(dispenser)

    # Assert
    assert len(repository._dispensers) == 0

@pytest.mark.asyncio
async def test_remove_dispenser_not_found() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    dispenser_to_remove = DispenserBuilder().build()
    repository = InMemoryDispenserRepository(dispensers=[dispenser])

    # Act
    await repository.delete(dispenser_to_remove)

    # Assert
    assert len(repository._dispensers) == 1

@pytest.mark.asyncio
async def test_update_dispenser_success() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    repository = InMemoryDispenserRepository(dispensers=[dispenser])
    dispenser.open_dispenser()

    # Act
    await repository.update(dispenser=dispenser)

    # Assert
    open_dispenser = repository._dispensers[0]
    assert open_dispenser.is_open == True
    assert open_dispenser.openings == 1
    assert open_dispenser.open_time != None
