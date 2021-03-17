import pytest

from pets.use_cases.list_pets import ListPets


class TestListPets:
    @pytest.mark.django_db
    def test_perfect(self, user_db, pet_db, user_pet_link_db):
        pets = ListPets().run(user=user_db)

        assert list(pets) == [pet_db]
