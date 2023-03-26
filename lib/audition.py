
class Audition:

    all_auditions = []

    def __init__(self, actor, location, role, hired=False):
        self.actor = actor
        self.location = location
        self.hired = hired
        self.role = role
        Audition.all_auditions.append(self)

    def call_back(self):
        self.hired = True

    def __repr__(self):
        return f"Audition(actors= '{self.actor}', location='{self.location}', role='{self.role.character_name}', hired={self.hired})"
