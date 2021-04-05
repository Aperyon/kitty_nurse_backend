import uuid

from django.db import models


class Pet(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255)
    official_name = models.CharField(max_length=255, blank=True, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(blank=True)
    species = models.CharField(max_length=255, blank=True, default="")
    breed = models.CharField(max_length=255, blank=True, default="")
    sex = models.CharField(max_length=255, blank=True, default="")
    color = models.CharField(max_length=255, blank=True, default="")
    chip_number = models.CharField(max_length=255, blank=True, default="")
    passport_number = models.CharField(max_length=255, blank=True, default="")
    owners = models.ManyToManyField("users.User", through="PetOwnership")


class PetOwnership(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    pet = models.ForeignKey("Pet", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)
