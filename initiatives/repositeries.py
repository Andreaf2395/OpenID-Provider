"""This code is completely tied to Django ORM but returns object of a class in entities.py (here of class Initiatives)
Thus we completely hide all the ORM details of the object """

from .entities import Initiative
from . models import ORMInitiative

class InitiativeRepo:

    def _decode_db_initiative(self, db_initiative):
        """This converts ORM db_initiative to entity initiative """

        return Initiative(init_id=db_initiative.init_id,
                        acronym=db_initiative.acronym,
                        full_name=db_initiative.full_name)

    def get_initiative(self, init_id):
        db_initiative = ORMInitiative.objects.get(init_id = init_id)
        return self._decode_db_initiative(db_initiative)

    def create_new_initiative(self, acronym, full_name):
        db_initiative = ORMInitiative.objects.create(acronym = acronym, full_name = full_name)
        return self._decode_db_initiative (db_initiative)

    def update_existing_initiative(self, init_id, acronym = None, full_name = None):
        orm_initiative = ORMInitiative.objects.get(init_id = init_id)

        orm_initiative.acronym = acronym
        orm_initiative.full_name = full_name

        orm_initiative.save()

        return self._decode_db_initiative (orm_initiative)

    def delete_existing_initiative(self, init_id):
        orm_initiative = ORMInitiative.objects.get(init_id = init_id)
        orm_initiative.delete()