import uuid
import pytest
from result import Err, Ok

from core.festival.application.command.remove_beer_command import RemoveBeerCommand
from core.festival.application.command.remove_beer_command_handler import RemoveBeerCommandHandler
from core.festival.domain.errors import BeerNotFoundError
from core.festival.infrastructure.services.inmemory_beer_repository import InMemoryBeerRepository
from core.festival.tests.beer_builder import BeerBuilder


@pytest.mark.asyncio
async def test_remove_beer_success() -> None:
    # Arrange
    beer = BeerBuilder().build()
    beer_repository = InMemoryBeerRepository(beers=[beer])
    handler = RemoveBeerCommandHandler(beer_repository)
    command = RemoveBeerCommand(id=beer.beer_id.value)

    # Act
    result = await handler.handle(command)

    # Assert
    assert isinstance(result, Ok)

@pytest.mark.asyncio
async def test_remove_beer_not_found() -> None:
    # Arrange
    beer_repository = InMemoryBeerRepository(beers=[])
    handler = RemoveBeerCommandHandler(beer_repository)
    command = RemoveBeerCommand(id=uuid.uuid4())

    # Act
    result = await handler.handle(command)

    # Assert
    assert isinstance(result, Err)
    assert isinstance(result.err(), BeerNotFoundError)
