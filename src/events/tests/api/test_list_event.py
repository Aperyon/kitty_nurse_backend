import pytest
from rest_framework import status
from rest_framework.reverse import reverse


class TestNoteListAPI:
    @pytest.mark.django_db
    def test_perfect(self, api_user_client, event_db):
        rv = api_user_client.get(reverse("event-list"))
        assert rv.status_code == status.HTTP_200_OK
        assert len(rv.data) == 1

    def test_unauthorized(self, api_client):
        rv = api_client.get(reverse("event-list"), {})

        assert rv.status_code == status.HTTP_403_FORBIDDEN
