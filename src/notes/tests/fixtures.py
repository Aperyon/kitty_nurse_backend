import pytest

from notes.models import Note


@pytest.fixture
def note(user, pet):
    return Note(user=user, pet=pet)
