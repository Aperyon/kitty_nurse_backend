import pytest
from rest_framework import status
from rest_framework.reverse import reverse


class TestNoteListAPI:
    @pytest.mark.django_db
    def test_perfect(self, api_user_client, note_db, pet_db):
        rv = api_user_client.get(reverse("note-detail", kwargs={"pk": note_db.pk}))

        assert rv.status_code == status.HTTP_200_OK
        assert rv.data["uuid"]
        assert rv.data["url"]
        assert rv.data["pet"] == reverse(
            "pet-detail",
            kwargs={"pk": pet_db.pk},
            request=rv.renderer_context["request"],
        )
        assert rv.data["description"] == "Lorem ipsum"
        assert rv.data["datetime"] is None

    @pytest.mark.django_db
    def test_not_own_note(self, api_user_client, note2_db):
        rv = api_user_client.get(reverse("note-detail", kwargs={"pk": note2_db.pk}))

        assert rv.status_code == status.HTTP_404_NOT_FOUND

    def test_unauthorized(self, api_client):
        rv = api_client.get(reverse("note-list"), {})

        assert rv.status_code == status.HTTP_403_FORBIDDEN
