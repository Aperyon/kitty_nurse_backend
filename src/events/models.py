import uuid

from django.db import models


class Event(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    pet = models.ForeignKey("pets.Pet", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, default="")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    datetime = models.DateTimeField(default=None, blank=True, null=True)
    event_type = models.ForeignKey(
        "EventType", on_delete=models.SET_NULL, null=True, blank=True
    )


class EventType(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    color = models.CharField(max_length=255, default="000")
    icon = models.CharField(max_length=255, blank=True, default="")
    name = models.CharField(max_length=255, default="")
