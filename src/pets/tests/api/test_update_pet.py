import pytest

from rest_framework import status
from rest_framework.reverse import reverse


class TestUpdatePetAPI:
    @pytest.mark.django_db
    def test_perfect(self, api_user_client, pet_db, user_pet_link_db, monkeypatch):
        url = reverse("pet-detail", kwargs={"pk": pet_db.uuid})
        payload = {}
        rv = api_user_client.patch(url, payload)

        assert rv.status_code == status.HTTP_200_OK

    def test_unauthorized(self, api_client, pet):
        rv = api_client.patch(reverse("pet-detail", kwargs={"pk": pet.uuid}), {})

        assert rv.status_code == status.HTTP_403_FORBIDDEN
