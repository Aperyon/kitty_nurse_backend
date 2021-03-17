from rest_framework.serializers import HyperlinkedModelSerializer

from pets.models import Pet
from pets.use_cases.create_pet import CreatePet
from pets.use_cases.update_pet import UpdatePet


class PetSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = (
            "url",
            "uuid",
            "name",
            "official_name",
            "date_of_birth",
            "image",
            "species",
            "breed",
            "sex",
            "color",
            "chip_number",
            "passport_number",
        )

    def create(self, validated_data):
        user = validated_data.pop("user")
        validated_data.update({"owners": [user]})
        pet = CreatePet().run(**validated_data)
        return pet

    def update(self, pet, validated_data):
        pet = UpdatePet().run(pet, self.context["request"].user, validated_data)
        return pet
