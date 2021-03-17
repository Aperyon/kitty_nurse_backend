from unittest.mock import Mock

import pytest
from rest_framework import status
from rest_framework.reverse import reverse


class TestListPetsAPI:
    @pytest.mark.django_db
    def test_perfect(self, api_user_client, user_pet_link_db, monkeypatch):
        url = reverse("pet-list")
        rv = api_user_client.get(url)

        assert rv.status_code == status.HTTP_200_OK
        assert len(rv.data) == 1
        assert rv.data[0]["uuid"]
        assert rv.data[0]["url"]
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
