from .audition import Audition

class Role:
    def __init__(self, character_name,):
        self.character_name = character_name

      
    @property
    def auditions(self):
        return [ audition for audition in Audition.all_auditions if audition.role == self]

    @property
    def actors(self):
        return [audition.actor for audition in self.auditions]

    @property
    def locations(self):
        return [audition.location for audition in self.auditions]

    @property
    def lead(self):
        for audition in self.auditions:
            if audition.hired:
                return audition
        return 'no actor has been hired for this role'

    @property
    def understudy(self):
        hired_actors = [audition for audition in self.auditions if audition.hired]
        if len(hired_actors) > 1:
            return hired_actors[-1]
        return 'no actor has been hired for understudy for this role'
    
