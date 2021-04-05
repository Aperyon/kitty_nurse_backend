import pytest
from rest_framework import status
from rest_framework.reverse import reverse


class TestCreatePet:
    @pytest.mark.django_db
    def test_perfect(self, api_user_client, monkeypatch):
        url = reverse("pet-list")
        payload = {"name": "Max", "species": "dog", "breed": "golden retriever"}
        rv = api_user_client.post(url, payload)

        assert rv.status_code == status.HTTP_201_CREATED, rv.data

        assert rv.data["uuid"]
        assert rv.data["url"]
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

        assert rv.status_code == status.HTTP_401_UNAUTHORIZED
