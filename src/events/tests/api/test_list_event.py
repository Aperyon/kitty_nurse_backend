import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from events.models import Event, EventType


class TestEventListAPI:
    @pytest.mark.django_db
    def test_perfect(self, api_user_client, event_db):
        rv = api_user_client.get(reverse("event-list"))
        assert rv.status_code == status.HTTP_200_OK
        assert len(rv.data) == 1

    def test_unauthorized(self, api_client):
        rv = api_client.get(reverse("event-list"), {})

        assert rv.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.django_db
    def test_without_filter(self, api_user_client, user_db, pet_db):
        et = EventType.objects.create(name="ET 1", user=user_db)
        Event.objects.create(user=user_db, event_type=et, pet=pet_db)
        Event.objects.create(user=user_db, event_type=None, pet=pet_db)

        rv = api_user_client.get(reverse("event-list"))

        assert rv.status_code == status.HTTP_200_OK
        assert len(rv.data) == 2

    @pytest.mark.django_db
    def test_filter_for_event_type(self, api_user_client, user_db, pet_db):
        et = EventType.objects.create(name="ET 1", user=user_db)
        Event.objects.create(user=user_db, event_type=et, pet=pet_db)
        Event.objects.create(user=user_db, event_type=None, pet=pet_db)

        rv = api_user_client.get(reverse("event-list") + f"?event_type={et.uuid}")

        assert rv.status_code == status.HTTP_200_OK
        assert len(rv.data) == 1

    @pytest.mark.django_db
    def test_filter_for_no_event_type(self, api_user_client, user_db, pet_db):
        et = EventType.objects.create(name="ET 1", user=user_db)
        Event.objects.create(user=user_db, event_type=et, pet=pet_db)
        e2 = Event.objects.create(user=user_db, event_type=None, pet=pet_db)

        rv = api_user_client.get(reverse("event-list") + "?event_type__isnull=true")

        assert rv.status_code == status.HTTP_200_OK
        assert len(rv.data) == 1
        assert rv.data[0]["uuid"] == str(e2.uuid)

    @pytest.mark.django_db
    def test_filter_for_has_event_type(self, api_user_client, user_db, pet_db):
        et = EventType.objects.create(name="ET 1", user=user_db)
        e1 = Event.objects.create(user=user_db, event_type=et, pet=pet_db)
        Event.objects.create(user=user_db, event_type=None, pet=pet_db)

        rv = api_user_client.get(reverse("event-list") + "?event_type__isnull=false")

        assert rv.status_code == status.HTTP_200_OK
        assert len(rv.data) == 1
        assert rv.data[0]["uuid"] == str(e1.uuid)
