from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
)

from pets.serializers import PetSerializer
from pets.use_cases.list_pets import ListPets


class PetViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = PetSerializer

    def get_queryset(self):
        return ListPets().run(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
