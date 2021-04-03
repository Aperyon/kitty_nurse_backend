from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from users.use_cases.signup_user import SignupUser


@api_view(["POST"])
@permission_classes([])
def signup_user_view(request):
    email = request.data.get("email")
    password = request.data.get("password")

    user, token = SignupUser().run(email, password)

    return Response({"token": token}, status=status.HTTP_201_CREATED)
