import pytest
from result import Err, Ok

from core.festival.application.command import CreateDispenserCommand, CreateDispenserCommandHandler
from core.festival.domain.errors import DispenserError
from core.festival.infrastructure.services.inmemory_dispenser_repository import InMemoryDispenserRepository


@pytest.mark.asyncio
async def test_create_dispenser_success() -> None:
    # Arrange
    dispenser_repository = InMemoryDispenserRepository(dipensers=[])
    handler = CreateDispenserCommandHandler(dispenser_repository=dispenser_repository)
    command = CreateDispenserCommand(beer_id="fa16fe7e-6a51-4572-9a6b-90fbdbad7c7d", flow_volume=2)

    # Act
    result = await handler.handle(command)

    # Assert
    assert isinstance(result, Ok)

@pytest.mark.asyncio
async def test_create_dispenser_with_invalid_flow_volume() -> None:
    # Arrange
    dispenser_repository = InMemoryDispenserRepository(dipensers=[])
    handler = CreateDispenserCommandHandler(dispenser_repository=dispenser_repository)
    command = CreateDispenserCommand(beer_id="fa16fe7e-6a51-4572-9a6b-90fbdbad7c7d", flow_volume=-2)

    # Act
    result = await handler.handle(command)

    # Assert
    assert isinstance(result, Err)
    assert isinstance(result.err(), DispenserError)
