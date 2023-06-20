from typing import List
import pytest

from result import Err, Ok

from core.festival.domain.dispenser import Dispenser, DispenserFactory
from core.festival.domain.errors import DispenserFlowVolumeRuleError, DispenserIsCloseRuleError, DispenserIsOpenRuleError
from core.festival.tests import BeerBuilder, DispenserBuilder
from core.festival.tests.dispenser_builder import DispenserOpenBuilder


INVALID_VOLUMES = [
    pytest.param(0, id="with flow volume equal 0"),
    pytest.param(-2, id="with negative flow volume"),
]

beer = BeerBuilder().build()


def test_build_dispenser_success() -> None:
    # Arrange
    # Act
    dispenser = DispenserFactory.build(beer_id=beer.beer_id.value, flow_volume=1)

    # Assert
    assert isinstance(dispenser, Ok)
    assert isinstance(dispenser.ok(), Dispenser)

@pytest.mark.parametrize("volumes", INVALID_VOLUMES)
def test_build_dispenser_with_invalid_flow_volume(volumes: List[float]):
    # Arrange
    # Act
    dispenser = DispenserFactory.build(beer_id=beer.beer_id.value, flow_volume=volumes)

    # Assert
    assert isinstance(dispenser, Err)
    assert isinstance(dispenser.err(), DispenserFlowVolumeRuleError)

def test_open_dispenser_sucess() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()

    # Act
    dispenser.open_dispenser()
    
    # Assert
    assert dispenser.is_open == True
    assert dispenser.openings == 1
    assert dispenser.open_time != None

def test_open_dispenser_when_the_dispenser_is_already_open() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()

    # Act
    dispenser.open_dispenser()
    result = dispenser.open_dispenser()
    
    # Assert
    assert isinstance(result, Err)
    assert isinstance(result.err(), DispenserIsOpenRuleError)

def test_close_dispenser_sucess() -> None:
    # Arrange
    dispenser = DispenserOpenBuilder().build()

    # Act
    dispenser.close_dispenser()
    
    # Assert
    assert dispenser.is_open == False
    assert dispenser.openings == 1
    assert dispenser.open_time == None

def test_close_dispenser_when_the_dispenser_is_already_close() -> None:
    # Arrange
    dispenser = DispenserBuilder().build()

    # Act
    result = dispenser.close_dispenser()
    
    # Assert
    assert isinstance(result, Err)
    assert isinstance(result.err(), DispenserIsCloseRuleError)

    