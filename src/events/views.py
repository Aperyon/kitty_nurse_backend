from rest_framework import viewsets

from events.serializers import EventSerializer, EventTypeSerializer
from events.models import Event, EventType


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventTypeSerializer

    def get_queryset(self):
        return EventType.objects.filter(user=self.request.user)
