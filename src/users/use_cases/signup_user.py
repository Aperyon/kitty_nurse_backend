from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from users.models import User


class SignupUser:
    def run(self, email, password):
        self.validate(email, password)

        user = User(email=email)
        user.set_password(password)

        self.persist(user)

        return user

    def validate(self, email, password):
        self.validate_email(email)
        self.validate_password(password)

    def validate_email(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError({"email": _("Email is not valid")})

        if self.check_user_with_same_email(email):
            raise ValidationError({"email": _("Email is already taken")})

    def validate_password(self, password):
        try:
            validate_password(password)
        except ValidationError:
            raise ValidationError({"password": _("Invalid password")})
        print("Valid password", password)

    def check_user_with_same_email(self, email):
        return User.objects.filter(email=email).exists()

    def persist(self, user):
        user.save()
