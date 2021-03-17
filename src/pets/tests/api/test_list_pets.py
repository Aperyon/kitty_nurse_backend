import pytest
from rest_framework import status
from rest_framework.reverse import reverse


pytestmark = pytest.mark.django_db


class TestListPetsAPI:
    def test_perfect(self, user_pet_link_db, api_user_client):
        url = reverse("pet-list")
        rv = api_user_client.get(url)

        assert rv.status_code == status.HTTP_200_OK

        assert len(rv.data) == 1
