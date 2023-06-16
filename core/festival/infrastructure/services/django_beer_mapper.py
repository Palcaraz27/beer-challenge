from core.festival.domain.beer import Beer, BeerId, BeerName
from festival.models import Beer as BeerModel


class DjangoBeerMapper:
    def to_domain(self, beer_instance: BeerModel) -> Beer:
        beer = Beer(
            id=BeerId(beer_instance.uuid),
            name=BeerName(beer_instance.name),
            price=beer_instance.price
        )

        return beer
