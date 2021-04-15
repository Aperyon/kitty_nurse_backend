from django.templatetags.static import static
from rest_framework import serializers

from events.models import Event, EventType


class EventSerializer(serializers.HyperlinkedModelSerializer):
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
        extra_kwargs = {
            "datetime": {"default": None},
            "title": {"required": True, "allow_blank": False},
        }


class EventTypeSerializer(serializers.HyperlinkedModelSerializer):
    icon_url = serializers.SerializerMethodField()

    class Meta:
        model = EventType
        fields = ["url", "uuid", "created_at", "name", "color", "icon_url"]

    def get_icon_url(self, instance):
        return self.context["request"].build_absolute_uri(static(instance.icon))
