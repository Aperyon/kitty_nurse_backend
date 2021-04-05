from events.models import EventType
from users.models import User


def create_event_type_preset_for_user(user: User):
    event_types = _get_event_type_preset()
    for event_type in event_types:
        event_type.user = user

    EventType.objects.bulk_create(event_types)


def _get_event_type_preset():
    return [
        EventType(name="Vet", color="#FF0000"),
        EventType(name="Vaccination", color="#00FF00"),
        EventType(name="School", color="#0000FF"),
        EventType(name="Walk", color="FFFF00"),
    ]
