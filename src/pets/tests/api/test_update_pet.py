from unittest.mock import Mock

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory

from pets.use_cases.update_pet import UpdatePet
from pets.views import PetViewSet


class TestUpdatePetAPI:
    def test_perfect(self, pet, user, monkeypatch):
        mock = Mock(return_value=pet)
        monkeypatch.setattr(UpdatePet, "run", mock)
        monkeypatch.setattr(PetViewSet, "get_object", lambda self: pet)

        url = reverse("pet-detail", kwargs={"pk": pet.uuid})
        payload = {}
        factory = APIRequestFactory()
        request = factory.patch(url, payload)
        request.user = user
        view = PetViewSet.as_view({"patch": "partial_update"})
        rv = view(request, pk=pet.uuid)

        assert rv.status_code == status.HTTP_200_OK
        mock.assert_called_once()

    def test_unauthorized(self, api_client, pet):
        rv = api_client.patch(reverse("pet-detail", kwargs={"pk": pet.uuid}), {})

        assert rv.status_code == status.HTTP_403_FORBIDDEN
