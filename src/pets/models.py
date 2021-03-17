import uuid

from django.db import models


class Pet(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255)
    official_name = models.CharField(max_length=255, blank=True, default="")
    date_of_birth = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    sex = models.CharField(max_length=255, blank=True, default="")
    color = models.CharField(max_length=255, blank=True, default="")
    chip_number = models.CharField(max_length=255, blank=True, default="")
    passport_number = models.CharField(max_length=255, blank=True, default="")