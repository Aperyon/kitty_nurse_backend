import pytest

from events.models import Event


@pytest.fixture
def event(user, pet):
    return Event(user=user, pet=pet, description="Lorem ipsum")


@pytest.fixture
def event2(user2, pet2):
    return Event(user=user2, pet=pet2, description="Lorem ipsum")


@pytest.fixture
def event_db(event):
    event.user.save()
    event.pet.save()
    event.save()
    return event


@pytest.fixture
def event2_db(event2):
    event2.user.save()
    event2.pet.save()
    event2.save()
    return event2
