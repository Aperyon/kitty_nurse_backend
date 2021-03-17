import pytest

from pets.models import Pet, PetOwnership


@pytest.fixture
def pet():
    return Pet(name="Max", species="dog", breed="golden retriever")


@pytest.fixture
def pet2():
    return Pet(name="Max2", species="dog2", breed="golden retriever2")


@pytest.fixture
def pet_db(pet):
    pet.save()
    return pet


@pytest.fixture
def pet2_db(pet2):
    pet2.save()
    return pet2


@pytest.fixture
def user_pet_link(pet, user):
    return PetOwnership(user=user, pet=pet)


@pytest.fixture
def user2_pet2_link(pet2, user2):
    return PetOwnership(user=user2, pet=pet2)


@pytest.fixture
def user_pet_link_db(pet_db, user_db):
    return PetOwnership.objects.create(user=user_db, pet=pet_db)


@pytest.fixture
def user2_pet2_link_db(pet2_db, user2_db):
    return PetOwnership.objects.create(user=user2_db, pet=pet2_db)
