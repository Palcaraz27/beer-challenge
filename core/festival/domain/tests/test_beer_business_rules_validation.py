
from typing import List
import pytest
from faker import Faker
from result import Err, Ok

from core.festival.domain.beer import Beer, BeerFactory
from core.festival.domain.errors import BeerNameLenghtRuleError, BeerPriceRuleError


INVALID_NAMES = [
    pytest.param("", id="with name that has 0 characters"),
    pytest.param(Faker().pystr(min_chars=41, max_chars=42), id="with name that has max characters"),
]
INVALID_PRICES = [
    pytest.param(0, id="with price equal 0"),
    pytest.param(-2, id="with negative price"),
]

def test_build_beer_success() -> None:
    # Arrange
    name = "beer-test"

    # Act
    beer = BeerFactory.build(name=name, price=2)

    # Assert
    assert isinstance(beer, Ok)
    assert isinstance(beer.ok(), Beer)

@pytest.mark.parametrize("names", INVALID_NAMES)
def test_build_beer_with_invalid_name(names: List[str]) -> None:
    # Arrange
    # Act
    beer = BeerFactory.build(name=names, price=2)

    # Assert
    assert isinstance(beer, Err)
    assert isinstance(beer.err(), BeerNameLenghtRuleError)

@pytest.mark.parametrize("prices", INVALID_PRICES)
def test_build_beer_with_invalid_price(prices: List[str]) -> None:
    # Arrange
    # Act
    beer = BeerFactory.build(name="test", price=prices)

    # Assert
    assert isinstance(beer, Err)
    assert isinstance(beer.err(), BeerPriceRuleError)
