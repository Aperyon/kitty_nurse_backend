import pytest
from rest_framework.test import APIClient


pytest_plugins = [
    "src.users.tests.fixtures",
    "src.pets.tests.fixtures",
    "src.events.tests.fixtures",
]


@pytest.fixture
def api_client():
    return APIClient()
