import pytest
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token

from users.use_cases.signup_user import SignupUser


class TestSignupUser:
    email = "test@email.com"
    password = "somecomplexpassword"

    @pytest.mark.django_db
    def test_perfect(self):
        SignupUser().run(self.email, self.password)

    @pytest.mark.django_db
    def test_taken_email(self, user_db):
        with pytest.raises(ValidationError):
            SignupUser().run(user_db.email, self.password)

    def test_invalid_email(self):
        with pytest.raises(ValidationError):
            SignupUser().run("invalid-email", self.password)

    @pytest.mark.django_db
    def test_invalid_password(self):
        with pytest.raises(ValidationError):
            SignupUser().run(self.email, "aaaaaa")

    @pytest.mark.django_db
    def test_creates_auth_token(self):
        SignupUser().run(self.email, self.password)
        assert Token.objects.all().exists()
