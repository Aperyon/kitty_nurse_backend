import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from pets.models import Pet


class TestCreatePet:
    @pytest.mark.django_db
    def test_perfect(self, user_db, api_user_client):
        url = reverse("pet-list")
        payload = {"name": "Max", "species": "dog", "breed": "golden retriever"}

        rv = api_user_client.post(url, payload)

        assert rv.status_code == status.HTTP_201_CREATED, rv.data

        assert Pet.objects.count() == 1
        pet = Pet.objects.first()

        assert rv.data["uuid"]
        assert rv.data["url"] == reverse(
            "pet-detail",
            kwargs={"pk": pet.uuid},
            request=rv.renderer_context["request"],
        )
        assert rv.data["name"] == "Max"
        assert rv.data["official_name"] == ""
        assert rv.data["date_of_birth"] is None
        assert rv.data["image"] is None
        assert rv.data["species"] == "dog"
        assert rv.data["breed"] == "golden retriever"
        assert rv.data["sex"] == ""
        assert rv.data["color"] == ""
        assert rv.data["chip_number"] == ""
        assert rv.data["passport_number"] == ""

        assert pet.name == "Max"
        assert pet.official_name == ""
        assert pet.date_of_birth is None
        assert bool(pet.image) is False
        assert pet.species == "dog"
        assert pet.breed == "golden retriever"
        assert pet.sex == ""
        assert pet.color == ""
        assert pet.chip_number == ""
        assert pet.passport_number == ""

        assert list(pet.owners.all()) == [user_db]
