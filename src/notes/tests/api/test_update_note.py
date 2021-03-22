import pytest
from rest_framework import status
from rest_framework.reverse import reverse


class TestNoteUpdateAPI:
    @pytest.mark.django_db
    def test_perfect(self, api_user_client, note_db, pet_db):
        rv = api_user_client.patch(
            reverse("note-detail", kwargs={"pk": note_db.uuid}),
            {"description": "Lorem ipsum2"},
        )

        assert rv.status_code == status.HTTP_200_OK
        assert rv.data["uuid"]
        assert rv.data["url"]
        assert rv.data["pet"] == reverse(
            "pet-detail",
            kwargs={"pk": pet_db.pk},
            request=rv.renderer_context["request"],
        )
        assert rv.data["description"] == "Lorem ipsum2"
        assert rv.data["datetime"] is None

    @pytest.mark.django_db
    def test_not_own_note(self, api_user_client, note2_db):
        rv = api_user_client.patch(reverse("note-detail", kwargs={"pk": note2_db.uuid}))

        assert rv.status_code == status.HTTP_404_NOT_FOUND

    def test_unauthorized(self, api_client, note):
        rv = api_client.patch(reverse("note-detail", kwargs={"pk": note.uuid}))

        assert rv.status_code == status.HTTP_403_FORBIDDEN
