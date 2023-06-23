import pytest
from result import Err, Ok

from core.festival.application.command import CloseDispenserCommand, CloseDispenserCommandHandler
from core.festival.domain.errors import DispenserIsCloseRuleError
from core.festival.infrastructure.services.inmemory_dispenser_repository import InMemoryDispenserRepository
from core.festival.tests.dispenser_builder import DispenserBuilder, DispenserOpenBuilder


@pytest.mark.asyncio
async def test_close_dispenser_success() -> None:
    # Arrange
    dispenser = DispenserOpenBuilder().build()
    dispenser_repository = InMemoryDispenserRepository(dispensers=[dispenser])
    handler = CloseDispenserCommandHandler(dispenser_repository)
    command = CloseDispenserCommand(id=dispenser.dispenser_id.value)

    # Act
    result = await handler.handle(command)

    # Assert
    assert isinstance(result, Ok)
    assert dispenser.is_open == False
    assert dispenser.openings == 1
    assert dispenser.open_time == None
    assert dispenser.total_open_time != None

@pytest.mark.asyncio
async def test_close_dispenser_fail_when_dispenser_already_close() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()
    dispenser_repository = InMemoryDispenserRepository(dispensers=[dispenser])
    handler = CloseDispenserCommandHandler(dispenser_repository)
    command = CloseDispenserCommand(id=dispenser.dispenser_id.value)

    # Act
    result = await handler.handle(command)

    # Assert
    assert isinstance(result, Err)
    assert isinstance(result.err(), DispenserIsCloseRuleError)
