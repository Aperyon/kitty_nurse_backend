from typing import List

from pets.models import Pet
from users.models import User


class ListPets:
    def run(self, *, user: User) -> List[Pet]:
        pets = self.get_by_user(user)
        return pets

    def get_by_user(self, user: User):
        return Pet.objects.filter(owners=user)
