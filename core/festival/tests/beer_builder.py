from core.festival.domain.beer import Beer, BeerId, BeerName


class BeerBuilder:
    _id: str
    _name: str
    _price: float

    def __init__(self) -> None:
        self._id = "123e4567-e89b-12d3-a456-526655440012"
        self._name = "Test Beer"
        self._price = 2

    def build(self) -> Beer:
        return Beer(
            id=BeerId(self._id),
            name=BeerName(self._name),
            price=self._price
        )
