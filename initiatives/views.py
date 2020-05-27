"""These classes get interactors from factories.py, parse the input parameters and format the output with serializers"""

from django.shortcuts import render

from . serializers import MultipleInitiativesSerializer, InitiativeSerializer

class InitiativeView(object):
    def __init__(self, get_initiative_interactor=None, create_new_initiative_interactor = None, update_existing_initiative_interactor = None, delete_existing_initiative_interactor = None):
        
        self.get_initiative_interactor = get_initiative_interactor
        self.create_new_initiative_interactor = create_new_initiative_interactor
        self.update_existing_initiative_interactor = update_existing_initiative_interactor
        self.delete_existing_initiative_interactor = delete_existing_initiative_interactor
    
    def get(self, init_id):
       
        initiative = self.get_initiative_interactor.set_params(init_id = init_id).execute()

        body = InitiativeSerializer.serialize(initiative)
        status = 200

        return body,status

    def post(self, acronym , full_name ):
       
        initiative = self.create_new_initiative_interactor.set_params(acronym = acronym, full_name = full_name).execute()
        body = InitiativeSerializer.serialize(initiative)
        status = 201

        return body,status

    def patch(self, init_id, acronym , full_name):
       
        initiative = self.update_existing_initiative_interactor.set_params(init_id = init_id, acronym= acronym, full_name= full_name).execute()

        body = InitiativeSerializer.serialize(initiative)
        status = 200

        return body,status

    def delete(self, init_id):
       
        self.delete_existing_initiative_interactor.set_params(init_id = init_id).execute()

        body = None
        status = 204

        return body,status