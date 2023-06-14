import uuid
from django.db import models

class Beer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self) -> str:
        return "Beer %s" % (self.name)
