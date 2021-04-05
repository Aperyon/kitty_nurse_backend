from rest_framework.serializers import HyperlinkedModelSerializer

from events.models import Event


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
        ]
        extra_kwargs = {"datetime": {"default": None}}
