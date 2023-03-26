from .audition import Audition

class Role:
    def __init__(self, character_name,):
        self.character_name = character_name
        self._auditions = []

    def add_audition(self, audition):
        self._auditions.append(audition)


    @property
    def actors(self):
        return [audition.actor for audition in self._auditions]

    @property
    def locations(self):
        return [audition.location for audition in self._auditions]

    @property
    def lead(self):
        for audition in self._auditions:
            if audition.hired:
                return audition
        return 'no actor has been hired for this role'

    @property
    def understudy(self):
        hired_auditions = [audition for audition in self._auditions if audition.hired]
        if len(hired_auditions) > 1:
            return hired_auditions[1]
        return 'no actor has been hired for understudy for this role'
    
