import logging
from typing import Optional

from core.festival.domain.dispenser import Dispenser, DispenserId
from core.festival.domain.dispenser_repository import DispenserRepository
from core.festival.infrastructure.services.django_beer_repository import DjangoBeerRepository
from core.festival.infrastructure.services.django_dispenser_mapper import DjangoDispenserMapper
from festival.models import Dispenser as DispenserModel


logger = logging.getLogger(__name__)


class DjangoDispenserRepository(DispenserRepository):
    def __init__(self) -> None:
        self.mapper = DjangoDispenserMapper()
        self.beer_repository = DjangoBeerRepository()

    async def save(self, dispenser: Dispenser) -> None:
        original_instance = await self._get_by_uuid(dispenser.dispenser_id.value)

        if original_instance is None:
            return await self._create_dispenser(dispenser)

        return original_instance

    async def get_by_id(self, dispenser_id: DispenserId) -> Optional[Dispenser]:
        instance = await self._get_by_uuid(dispenser_id.value)
        return self.mapper.to_domain(instance) if instance else None

    async def _get_by_uuid(self, dispenser_uuid: str) -> Optional[DispenserModel]:
        try:
            instance = await DispenserModel.objects.select_related("beer").aget(uuid=dispenser_uuid)
            return instance
        except DispenserModel.DoesNotExist:
            logger.warning("Error getting dispenser: {uuid} does not exist".format(uuid=dispenser_uuid))
            return None

    async def _create_dispenser(self, dispenser: Dispenser) -> None:
        beer = await self.beer_repository.get_by_uuid(dispenser.beer_id.value)
        if beer is None:
            logger.warning("Error getting beer: {uuid} does not exist".format(uuid=dispenser.beer_id.value))
            logger.warning("The dispenser could not be created because the beer does not exist.")
            return None

        await DispenserModel.objects.acreate(
            uuid=dispenser.dispenser_id.value,
            beer=beer,
            flow_volume=dispenser.flow_volume
        )

