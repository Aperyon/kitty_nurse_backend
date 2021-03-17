import datetime as dt

from notes.models import Note
from pets.models import Pet
from users.models import User
from pets.exceptions import NotOwnPet


class CreateNote:
    def run(
        self, *, pet: Pet, user: User, datetime: dt.datetime, description: str
    ) -> Note:
        self.validate(pet, user, datetime, description)
        note = Note(pet=pet, user=user, description=description, datetime=datetime)
        self.persist(note)
        return note

    def validate(self, pet: Pet, user: User, datetime: dt.datetime, description: str):
        if not self.check_owner(pet, user):
            raise NotOwnPet

    def check_owner(self, pet: Pet, user: User) -> bool:
        return user in pet.owners.all()

    def persist(self, note: Note):
        note.save()
