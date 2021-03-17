import datetime as dt
from unittest.mock import Mock

import pytest

from pets.models import Pet
from pets.use_cases.create_pet import CreatePet


@pytest.fixture
def mock_persist(monkeypatch):
    mock = Mock()
    monkeypatch.setattr(CreatePet, "persist", mock)
    return mock


def create_pet_data(**overrides):
    data = {
        "name": "Max",
        "official_name": "Pearl of Hunters Keep Calm",
        "date_of_birth": dt.date.today(),
        "image": None,
        "species": "dog",
        "breed": "golden retriever",
        "sex": "male",
        "color": "creme",
        "chip_number": "",
        "passport_number": "",
        "owners": [],
    }
    data.update(overrides)
    return data


class TestCreatePet:
    def test_perfect(self, mock_persist):
        pet = CreatePet().run(**create_pet_data())

        assert isinstance(pet, Pet)
        assert pet.name == "Max"
        assert pet.official_name == "Pearl of Hunters Keep Calm"
        assert pet.date_of_birth == dt.date.today()
        assert bool(pet.image) is False
        assert pet.species == "dog"
        assert pet.breed == "golden retriever"
        assert pet.sex == "male"
        assert pet.color == "creme"
        assert pet.chip_number == ""
        assert pet.passport_number == ""

    @pytest.mark.django_db
    def test_adds_owner(self, user):
        user.save()

        pet = CreatePet().run(**create_pet_data(owners=[user]))

        assert list(pet.owners.all()) == [user]
