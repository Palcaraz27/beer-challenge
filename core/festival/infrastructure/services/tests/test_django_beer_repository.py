import pytest

from core.festival.tests.beer_builder import BeerBuilder
from ..django_beer_repository import DjangoBeerRepository


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test_save_success() -> None:
    # Arrange
    django_repository = DjangoBeerRepository()
    beer = BeerBuilder().build()

    # Act
    await django_repository.save(beer)

    # Assert
    beer_found = await django_repository.get_by_id(beer_id=beer.beer_id)
    assert beer_found
