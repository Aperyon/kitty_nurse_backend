import pytest
from django.utils import timezone

from notes.use_cases.create_note import CreateNote
from notes.models import Note
from pets.exceptions import NotOwnPet


def create_note_data(**overrides):
    data = {
        "user": None,
        "pet": None,
        "datetime": timezone.now(),
        "description": "lorem ipsum dolor sit amet",
    }
    data.update(overrides)
    return data


class TestCreateNote:
    @pytest.mark.django_db
    def test_perfect(self, user_db, pet_db, user_pet_link_db):
        note = CreateNote().run(**create_note_data(user=user_db, pet=pet_db))

        assert isinstance(note, Note)
        assert note.user == user_db
        assert note.pet == pet_db
        assert note.datetime
        assert note.description == "lorem ipsum dolor sit amet"

    @pytest.mark.django_db
    def test_not_own_pet(self, user_db, pet_db):
        with pytest.raises(NotOwnPet):
            CreateNote().run(**create_note_data(user=user_db, pet=pet_db))
