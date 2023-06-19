from django.test import TestCase
import pytest

from core.festival.tests.beer_builder import BeerBuilder
from ..django_beer_repository import DjangoBeerRepository


class DjangoRepositoryTestCase(TestCase):
    @pytest.mark.asyncio
    async def test_save_success(self) -> None:
        # Arrange
        django_repository = DjangoBeerRepository()
        beer = BeerBuilder().build()

        # Act
        await django_repository.save(beer)

        # Assert
        beer_found = await django_repository.get_by_id(beer_id=beer.beer_id)
        assert beer_found


    @pytest.mark.asyncio
    async def test_get_all_success(self) -> None:
        # Arrange
        django_repository = DjangoBeerRepository()

        # Act
        result = await django_repository.get_all()

        # Assert
        assert len(result) == 1
        assert result[0].name.value == "Estrella Levante"
