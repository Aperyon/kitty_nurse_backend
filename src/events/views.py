from rest_framework import viewsets

from events.filters import EventFilter
from events.models import Event, EventType
from events.serializers import EventSerializer, EventTypeSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    filterset_class = EventFilter

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventTypeSerializer

    def get_queryset(self):
        return EventType.objects.filter(user=self.request.user)
