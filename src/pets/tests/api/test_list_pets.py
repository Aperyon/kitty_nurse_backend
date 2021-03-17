from unittest.mock import Mock

import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory

from pets.use_cases.list_pets import ListPets
from pets.views import PetViewSet


class TestListPetsAPI:
    def test_perfect(self, user, pet, monkeypatch):
        mock = Mock(return_value=[pet])
        monkeypatch.setattr(ListPets, "run", mock)

        factory = APIRequestFactory()
        url = reverse("pet-list")
        request = factory.get(url)
        view = PetViewSet.as_view({"get": "list"})
        request.user = user
        rv = view(request)

        mock.assert_called_once()
        assert rv.status_code == status.HTTP_200_OK
        assert len(rv.data) == 1

        assert rv.data[0]["uuid"]
        assert rv.data[0]["url"] == reverse(
            "pet-detail",
            kwargs={"pk": pet.uuid},
            request=rv.renderer_context["request"],
        )
        assert rv.data[0]["name"] == "Max"
        assert rv.data[0]["official_name"] == ""
        assert rv.data[0]["date_of_birth"] is None
        assert rv.data[0]["image"] is None
        assert rv.data[0]["species"] == "dog"
        assert rv.data[0]["breed"] == "golden retriever"
        assert rv.data[0]["sex"] == ""
        assert rv.data[0]["color"] == ""
        assert rv.data[0]["chip_number"] == ""
        assert rv.data[0]["passport_number"] == ""
        assert len(rv.data[0].keys()) == 12

    def test_unauthorized(self, api_client):
        url = reverse("pet-list")

        rv = api_client.get(url)

        assert rv.status_code == status.HTTP_403_FORBIDDEN
