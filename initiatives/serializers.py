"""Return body in form of a python dictionary """

class InitiativeSerializer:
    @staticmethod
    def serialize(initiative):
        return {
            'init_id': int(initiative.init_id),
            'acronym': initiative.acronym,
            'full_name': initiative.full_name
        }

class MultipleInitiativesSerializer:

    @staticmethod
    def serialize(initiatives):
        return [InitiativeSerializer.serialize(initiative) for initiative in initiatives]