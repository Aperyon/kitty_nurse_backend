import datetime as dt
from typing import List

from django.utils import timezone

from pets.models import Pet, PetOwnership
from users.models import User


class CreatePet:
    def run(
        self,
        *,
        name: str,
        official_name: str = "",
        date_of_birth: dt.date = None,
        image: str = "",
        species: str = "",
        breed: str = "",
        sex: str = "",
        color: str = "",
        chip_number: str = "",
        passport_number: str = "",
        owners: List[User] = None,
    ) -> Pet:
        print("Image", image)
        if owners is None:
            owners = []

        pet = Pet(
            name=name,
            official_name=official_name,
            date_of_birth=date_of_birth,
            image=image,
            species=species,
            breed=breed,
            sex=sex,
            color=color,
            chip_number=chip_number,
            passport_number=passport_number,
        )

        ownerships = []
        for owner in owners:
            ownership = PetOwnership(pet=pet, user=owner, start=timezone.now())
            ownerships.append(ownership)

        self.persist(pet, ownerships)
        return pet

    def persist(self, pet: Pet, ownerships: List[PetOwnership]) -> Pet:
        pet.save()

        for ownership in ownerships:
            ownership.save()

        return pet
