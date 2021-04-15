from django_filters import rest_framework as filters

from events.models import Event


class EventFilter(filters.FilterSet):
    class Meta:
        model = Event
        fields = {"event_type": ["exact", "isnull"], "pet": ["exact"]}
