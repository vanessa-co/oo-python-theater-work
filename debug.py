import ipdb
from lib import *

# Test your code below...
role1 = Role("Bad Guy")
role2 = Role("Good Guy")
role3 = Role("Ok Guy")

audition1 = Audition("George Clooney", "Los Angeles", role1)
audition2 = Audition("Brad Pitt", "New York", role2)
audition3 = Audition("Chris Pine", "Los Angeles", role3)
audition4 = Audition("Matt Damon", "New York", role2)


# the below line allows us to stop & try stuff!
ipdb.set_trace()