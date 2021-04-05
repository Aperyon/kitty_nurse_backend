from rest_framework.serializers import HyperlinkedModelSerializer

from events.models import Event, EventType


class EventSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = [
            "url",
            "uuid",
            "title",
            "description",
            "created_at",
            "datetime",
            "description",
            "pet",
            "event_type",
        ]
        extra_kwargs = {"datetime": {"default": None}}


class EventTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = EventType
        fields = ["url", "uuid", "created_at", "name", "color", "icon"]
