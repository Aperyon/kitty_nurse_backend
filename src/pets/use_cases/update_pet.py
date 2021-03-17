from pets.exceptions import NotOwnPet
from pets.models import Pet
from users.models import User


class UpdatePet:
    def run(self, pet: Pet, user: User, update_values) -> Pet:
        self.validate(pet, user, update_values)

        for field, value in update_values.items():
            setattr(pet, field, value)

        print("Pet", pet)
        self.persist(pet)

        return pet

    def validate(self, pet: Pet, user: User, update_values):
        update_values.pop("uuid", None)

        if not self.check_owner(pet, user):
            raise NotOwnPet()

    def check_owner(self, pet: Pet, user: User) -> bool:
        return user in pet.owners.all()

    def persist(self, pet: Pet) -> Pet:
        pet.save()
        return pet
