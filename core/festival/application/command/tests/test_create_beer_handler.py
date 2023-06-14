import pytest
from result import Ok
from core.festival.application.command.create_beer_command import CreateBeerCommand
from core.festival.application.command.create_beer_command_handler import CreateBeerCommandHandler
from core.festival.domain.errors import BeerError
from core.festival.infrastructure.services.inmemory_beer_repository import InMemoryBeerRepository


@pytest.mark.asyncio
async def test_create_beer_success() -> None:
    # Arrange
    beer_repository = InMemoryBeerRepository(beers=[])
    handler = CreateBeerCommandHandler(beer_repository)
    command = CreateBeerCommand(name="test", price=2)

    # Act
    result = await handler.handle(command)

    # Assert
    assert isinstance(result, Ok)

@pytest.mark.asyncio
async def test_create_beer_with_invalid_name() -> None:
    # Arrange
    beer_repository = InMemoryBeerRepository(beers=[])
    handler = CreateBeerCommandHandler(beer_repository)
    command = CreateBeerCommand(name="", price=2)

    # Act
    result = await handler.handle(command)

    # Assert
    assert isinstance(result, BeerError)
