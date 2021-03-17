import uuid

from django.db import models


class Note(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    pet = models.ForeignKey("pets.Pet", on_delete=models.CASCADE)
    description = models.TextField(blank=True, default="")
    datetime = models.DateTimeField()