from result import Err, Ok, Result
from core.festival.domain.beer import BeerFactory
from core.festival.domain.beer_repository import BeerRepository
from core.festival.domain.errors import BeerError
from festival.cqrs.models import CommandHandler
from .create_beer_command import CreateBeerCommand


class CreateBeerCommandHandler(CommandHandler[CreateBeerCommand]):
    def __init__(self, beer_repository: BeerRepository) -> None:
        self._beer_repository = beer_repository

    async def handle(self, command: CreateBeerCommand) -> Result[None, BeerError]:
        beer_name = command.name
        beer_price = command.price

        beer = BeerFactory.build(name=beer_name, price=beer_price)

        if isinstance(beer, Err):
            return beer.err()

        await self._beer_repository.save(beer)
        
        return Ok()
