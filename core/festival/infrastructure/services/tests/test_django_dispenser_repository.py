import uuid
import pytest
from django.test import TestCase
from asgiref.sync import async_to_sync

from core.festival.domain.dispenser import DispenserId
from core.festival.infrastructure.services.django_beer_repository import DjangoBeerRepository
from core.festival.infrastructure.services.django_dispenser_repository import DjangoDispenserRepository
from core.festival.tests.beer_builder import BeerBuilder
from core.festival.tests.dispenser_builder import DispenserBuilder


class DjangoRepositoryTestCase(TestCase):
    def setUp(self):
        async def async_setup():
            self.beer_repository = DjangoBeerRepository()
            self.beer = BeerBuilder().build()
            await self.beer_repository.save(self.beer)

        async_to_sync(async_setup)()
        

    @pytest.mark.asyncio
    async def test_save_success(self) -> None:
        # Arrange
        dispenser_repository = DjangoDispenserRepository()
        dispenser = DispenserBuilder().build_with_beer(self.beer.beer_id.value)

        # Act
        await dispenser_repository.save(dispenser)

        # Assert
        dispenser_found = await dispenser_repository.get_by_id(dispenser.dispenser_id)
        assert dispenser_found

    @pytest.mark.asyncio
    async def test_get_all_success(self) -> None:
        # Arrange
        django_repository = DjangoDispenserRepository()
        dispenser = DispenserBuilder().build_with_beer(self.beer.beer_id.value)
        await django_repository.save(dispenser)

        # Act
        result = await django_repository.get_all()

        # Assert
        assert len(result) == 1

    @pytest.mark.asyncio
    async def test_get_by_id_success(self) -> None:
        # Arrange
        django_repository = DjangoDispenserRepository()
        dispenser = DispenserBuilder().build_with_beer(self.beer.beer_id.value)
        await django_repository.save(dispenser)

        # Act
        result = await django_repository.get_by_id(dispenser_id=dispenser.dispenser_id)

        # Assert
        assert result

    @pytest.mark.asyncio
    async def test_get_by_id_not_found(self) -> None:
        # Arrange
        django_repository = DjangoDispenserRepository()

        # Act
        result = await django_repository.get_by_id(dispenser_id=DispenserId(uuid.uuid4()))

        # Assert
        assert result is None

    @pytest.mark.asyncio
    async def test_update_dispenser_success(self) -> None:
        # Arrange
        django_repository = DjangoDispenserRepository()
        dispenser = DispenserBuilder().build_with_beer(self.beer.beer_id.value)
        await django_repository.save(dispenser)
        dispenser.open_dispenser()

        # Act
        await django_repository.update(dispenser)

        # Assert
        assert dispenser.is_open == True
        assert dispenser.openings == 1
        assert dispenser.open_time != None
