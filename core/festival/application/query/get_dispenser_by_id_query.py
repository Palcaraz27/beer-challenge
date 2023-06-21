from dataclasses import dataclass

from app.cqrs.models import Query


@dataclass(frozen=True)
class GetDispenserByIdQuery(Query):
    id: str
