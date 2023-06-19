from result import Err, Ok, Result
from app.cqrs.models import CommandHandler
from core.festival.application.command.remove_beer_command import RemoveBeerCommand
from core.festival.domain.beer import BeerId
from core.festival.domain.beer_repository import BeerRepository
from core.festival.domain.errors import BeerError, BeerNotFoundError


class RemoveBeerCommandHandler(CommandHandler[RemoveBeerCommand]):
    def __init__(self, beer_repository: BeerRepository) -> None:
        self._beer_repository = beer_repository

    async def handle(self, command: RemoveBeerCommand) -> Result[None, BeerError]:
        beer = await self._beer_repository.get_by_id(BeerId(command.id))

        if beer is None:
            return Err(BeerNotFoundError(command.id))

        await self._beer_repository.delete(beer)

        return Ok()
