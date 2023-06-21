import datetime
import uuid
from django.db import models

class Beer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self) -> str:
        return "Beer %s" % (self.name)


class Dispenser(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    beer = models.ForeignKey("Beer", on_delete=models.CASCADE)
    flow_volume = models.FloatField()
    is_open = models.BooleanField(default=False)
    openings = models.IntegerField(default=0)
    total_open_time = models.TimeField(default=datetime.time(0, 0, 0))
    open_time = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return "Dispenser %s" % (self.uuid)
