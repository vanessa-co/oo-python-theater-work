
class Audition:
    def __init__(self, actor, location, role, hired=False):
        self.actor = actor
        self.location = location
        self.hired = hired
        self._role = role
        role.add_audition(self)

    def call_back(self):
        self.hired = True
