from rest_framework.serializers import HyperlinkedModelSerializer

from notes.models import Note
from notes.use_cases.create_note import CreateNote


class NoteSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ["url", "uuid", "pet", "datetime", "description"]
        extra_kwargs = {"datetime": {"default": None}}

    def create(self, validated_data):
        print("Validated", validated_data)
        note = CreateNote().run(**validated_data)
        return note
