import pytest
from rest_framework import status
from rest_framework.reverse import reverse


class TestCreateNoteAPI:
    @pytest.mark.django_db
    def test_perfect(
        self, user_db, pet_db, user_pet_link_db, api_user_client, monkeypatch
    ):
        url = reverse("event-list")
        pet_url = reverse("pet-detail", kwargs={"pk": pet_db.pk})
        payload = {
            "pet": pet_url,
            "description": "lorem ipsum dolor sit amet",
        }
        rv = api_user_client.post(url, payload)

        assert rv.status_code == status.HTTP_201_CREATED, rv.data

        assert rv.data["uuid"]
        assert rv.data["url"]
        assert rv.data["pet"]
        assert rv.data["datetime"] is None
        assert rv.data["description"] == "lorem ipsum dolor sit amet"
        assert len(rv.data.keys()) == 5

    def test_unauthorized(self, api_client):
        rv = api_client.post(reverse("event-list"), {})

        assert rv.status_code == status.HTTP_403_FORBIDDEN
