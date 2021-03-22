from rest_framework import viewsets

from notes.serializers import NoteSerializer
from notes.models import Note


class NoteViewSet(viewsets.ModelViewSet,):
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
