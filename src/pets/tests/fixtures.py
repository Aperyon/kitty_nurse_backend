import pytest

from pets.models import Pet, PetOwnership


@pytest.fixture
def pet():
    return Pet(name="Max", species="dog", breed="golden retriever")


@pytest.fixture
def pet_db(pet):
    pet.save()
    return pet


@pytest.fixture
def user_pet_link(pet, user):
    return PetOwnership(user=user, pet=pet)


@pytest.fixture
def user_pet_link_db(pet_db, user_db):
    return PetOwnership.objects.create(user=user_db, pet=pet_db)
