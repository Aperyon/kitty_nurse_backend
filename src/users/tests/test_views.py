from unittest.mock import Mock

from rest_framework import status
from rest_framework.reverse import reverse

from users.use_cases.signup_user import SignupUser


class TestSignup:
    def test_call_signup_use_case(self, api_client, monkeypatch):
        mock_signup = Mock()
        monkeypatch.setattr(SignupUser, "run", mock_signup)
        rv = api_client.post(
            reverse("signup"), {"email": "test@email.com", "password": "somepassword"}
        )

        assert rv.status_code == status.HTTP_201_CREATED
        mock_signup.assert_called_once_with("test@email.com", "somepassword")
