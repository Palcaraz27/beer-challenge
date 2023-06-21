import pytest
from django.test import TestCase
from core.festival.infrastructure.services.django_beer_repository import DjangoBeerRepository

from core.festival.infrastructure.services.django_dispenser_repository import DjangoDispenserRepository
from core.festival.tests.beer_builder import BeerBuilder
from core.festival.tests.dispenser_builder import DispenserBuilder


class DjangoRepositoryTestCase(TestCase):
    @pytest.mark.asyncio
    async def test_save_success(self) -> None:
        # Arrange
        beer_repository = DjangoBeerRepository()
        beer = BeerBuilder().build()
        dispenser_repository = DjangoDispenserRepository()
        dispenser = DispenserBuilder().build_with_beer(beer.beer_id.value)
        await beer_repository.save(beer)

        # Act
        await dispenser_repository.save(dispenser)

        # Assert
        dispenser_found = await dispenser_repository.get_by_id(dispenser.dispenser_id)
        assert dispenser_found
