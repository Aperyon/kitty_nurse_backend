import uuid
from unittest.mock import Mock

import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory

from pets.models import Pet
from pets.use_cases.create_pet import CreatePet
from pets.views import PetViewSet


class TestCreatePet:
    def test_perfect(self, user, pet, monkeypatch):
        mock = Mock(return_value=pet)
        monkeypatch.setattr(CreatePet, "run", mock)

        url = reverse("pet-list")
        payload = {"name": "Max", "species": "dog", "breed": "golden retriever"}
        factory = APIRequestFactory()
        request = factory.post(url, payload)
        request.user = user
        rv = PetViewSet.as_view({"post": "create"})(request)

        assert rv.status_code == status.HTTP_201_CREATED, rv.data

        mock.assert_called_once()

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
        assert len(rv.data.keys()) == 12

    def test_unauthorized(self, api_client):
        rv = api_client.post(reverse("pet-list"), {})

        assert rv.status_code == status.HTTP_403_FORBIDDEN
