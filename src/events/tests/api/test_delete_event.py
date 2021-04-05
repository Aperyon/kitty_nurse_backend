import pytest
from rest_framework import status
from rest_framework.reverse import reverse


class TestNoteDeleteAPI:
    @pytest.mark.django_db
    def test_perfect(self, api_user_client, event_db, pet_db):
        rv = api_user_client.delete(
            reverse("event-detail", kwargs={"pk": event_db.uuid}),
            {"description": "Lorem ipsum2"},
        )

        assert rv.status_code == status.HTTP_204_NO_CONTENT

    @pytest.mark.django_db
    def test_not_own_event(self, api_user_client, event2_db):
        rv = api_user_client.delete(
            reverse("event-detail", kwargs={"pk": event2_db.uuid})
        )

        assert rv.status_code == status.HTTP_404_NOT_FOUND

    def test_unauthorized(self, api_client, event):
        rv = api_client.delete(reverse("event-detail", kwargs={"pk": event.uuid}))

        assert rv.status_code == status.HTTP_403_FORBIDDEN
