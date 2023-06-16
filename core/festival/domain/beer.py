import uuid
from dataclasses import dataclass

from result import Err, Ok, Result

from .errors import BeerError, BeerNameLenghtRuleError, InvalidBeerIdError


BEER_NAME_MAX_LENGHT = 20

@dataclass(frozen=True)
class BeerId:
    value: str

    @classmethod
    def from_string(cls, value: str) -> "BeerId":
        if not isinstance(value, str):
            raise InvalidBeerIdError

        return cls(value)

    @classmethod
    def random(cls) -> "BeerId":
        return cls(str(uuid.uuid4()))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, BeerId) and self.value == other.value


@dataclass(frozen=True)
class BeerName:
    value: str

    def __eq__(self, other: object) -> bool:
        return isinstance(other, BeerName) and self.value == other.value


class Beer:
    _id: BeerId
    _name: BeerName
    _price: float

    def __init__(self, id: BeerId, name: BeerName, price: float) -> None:
        self._id = id
        self._name = name
        self._price = price

    @property
    def beer_id(self) -> BeerId:
        return self._id

    @property
    def name(self) -> BeerName:
        return self._name

    @property
    def price(self) -> float:
        return self._price


class BeerFactory:
    @staticmethod
    def build(name: str, price: float) -> Result[Beer, BeerError]:
        if not (0 < len(name) <= BEER_NAME_MAX_LENGHT):
            return Err(BeerNameLenghtRuleError())

        return Ok(Beer(id=BeerId.random(), name=BeerName(name), price=price))
