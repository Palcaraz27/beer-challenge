import pytest
from result import Err, Ok

from core.festival.application.command import OpenDispenserCommand, OpenDispenserCommandHandler
from core.festival.domain.errors import DispenserIsOpenRuleError
from core.festival.infrastructure.services.inmemory_dispenser_repository import InMemoryDispenserRepository
from core.festival.tests.dispenser_builder import DispenserBuilder, DispenserOpenBuilder


@pytest.mark.asyncio
async def test_open_dispenser_success() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    dispenser_repository = InMemoryDispenserRepository(dispensers=[dispenser])
    handler = OpenDispenserCommandHandler(dispenser_repository)
    command = OpenDispenserCommand(id=dispenser.dispenser_id.value)

    # Act
    result = await handler.handle(command)

    # Assert
    assert isinstance(result, Ok)
    assert dispenser.is_open == True
    assert dispenser.openings == 1
    assert dispenser.open_time != None

@pytest.mark.asyncio
async def test_open_dispenser_fail_when_dispenser_already_open() -> None:
    # Arrange
    dispenser = DispenserOpenBuilder().build()
    dispenser_repository = InMemoryDispenserRepository(dispensers=[dispenser])
    handler = OpenDispenserCommandHandler(dispenser_repository)
    command = OpenDispenserCommand(id=dispenser.dispenser_id.value)

    # Act
    result = await handler.handle(command)

    # Assert
    assert isinstance(result, Err)
    assert isinstance(result.err(), DispenserIsOpenRuleError)
