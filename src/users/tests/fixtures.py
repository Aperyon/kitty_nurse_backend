import pytest
from rest_framework.test import APIClient

from users.models import User


@pytest.fixture
def user():
    user = User(email="test@email.com")
    user.set_password("some_complex_passowrd")
    return user


@pytest.fixture
def user2():
    user = User(email="test2@email.com")
    user.set_password("some_complex_passowrd")
    return user


@pytest.fixture
def user_db(user):
    user.save()
    return user


@pytest.fixture
def user2_db(user2):
    user2.save()
    return user2


@pytest.fixture
def api_user_client(user_db):
    client = APIClient()
    client.force_authenticate(user=user_db)

    return client


@pytest.fixture
def api_user2_client(user2_db):
    client = APIClient()
    client.force_authenticate(user=user2_db)

    return client
