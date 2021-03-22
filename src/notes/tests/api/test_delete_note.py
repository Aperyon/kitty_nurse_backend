import pytest
from rest_framework import status
from rest_framework.reverse import reverse


class TestNoteDeleteAPI:
    @pytest.mark.django_db
    def test_perfect(self, api_user_client, note_db, pet_db):
        rv = api_user_client.delete(
            reverse("note-detail", kwargs={"pk": note_db.uuid}),
            {"description": "Lorem ipsum2"},
        )

        assert rv.status_code == status.HTTP_204_NO_CONTENT

    @pytest.mark.django_db
    def test_not_own_note(self, api_user_client, note2_db):
        rv = api_user_client.delete(
            reverse("note-detail", kwargs={"pk": note2_db.uuid})
        )

        assert rv.status_code == status.HTTP_404_NOT_FOUND

    def test_unauthorized(self, api_client, note):
        rv = api_client.delete(reverse("note-detail", kwargs={"pk": note.uuid}))

        assert rv.status_code == status.HTTP_403_FORBIDDEN
