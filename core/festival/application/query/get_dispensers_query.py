from dataclasses import dataclass

from app.cqrs.models import Query


@dataclass
class GetDispensersQuery(Query):
    ...

