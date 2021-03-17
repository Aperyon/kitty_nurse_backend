import datetime as dt
from unittest.mock import Mock

import pytest

from pets.use_cases.update_pet import UpdatePet
from pets.exceptions import NotOwnPet


@pytest.fixture
def mock_persist(monkeypatch):
    mock = Mock()
    monkeypatch.setattr(UpdatePet, "persist", mock)
    return mock


@pytest.fixture
def mock_check_owner(monkeypatch):
    mock = Mock(return_value=True)
    monkeypatch.setattr(UpdatePet, "check_owner", mock)
    return mock


class TestUpdatePet:
    @pytest.mark.django_db
    def test_saves_to_db(self, pet_db, user_db, user_pet_link_db):
        pet = UpdatePet().run(pet_db, user_db, {"name": "New name"})

        pet.refresh_from_db()
        assert pet.name == "New name"

    @pytest.mark.django_db
    def test_can_not_update_others_pet(self, user_db, pet2_db, user2_pet2_link_db):
        with pytest.raises(NotOwnPet):
            UpdatePet().run(pet2_db, user_db, {"name": "New name"})

    def test_update_multiple_values(self, pet, user, mock_persist, mock_check_owner):
        new_date = dt.date.today()
        pet = UpdatePet().run(
            pet, user, {"date_of_birth": new_date, "official_name": "official name"}
        )

        assert pet.date_of_birth == new_date
        assert pet.official_name == "official name"

    def test_uuid_can_not_be_updated(self, pet, user, mock_persist, mock_check_owner):
        original_uuid = pet.uuid
        pet = UpdatePet().run(pet, user, {"uuid": "new value"})

        assert pet.uuid == original_uuid
        assert pet.uuid != "new value"
