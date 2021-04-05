import pytest

from notes.models import Note


@pytest.fixture
def note(user, pet):
    return Note(user=user, pet=pet, description="Lorem ipsum")


@pytest.fixture
def note2(user2, pet2):
    return Note(user=user2, pet=pet2, description="Lorem ipsum")


@pytest.fixture
def note_db(note):
    note.user.save()
    note.pet.save()
    note.save()
    return note


@pytest.fixture
def note2_db(note2):
    note2.user.save()
    note2.pet.save()
    note2.save()
    return note2
