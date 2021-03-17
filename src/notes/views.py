from rest_framework import viewsets
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin

from notes.serializers import NoteSerializer


class NoteViewSet(RetrieveModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
