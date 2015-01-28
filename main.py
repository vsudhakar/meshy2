# Main Simulation File

# Used libraries
import simpy

# Local modules
from networkDevice import *
from eventBuffer import *

# Simulation
env = simpy.Environment()
eb = eventBuffer(env)

d1 = networkDevice(1, "HELLOWORLD", env, eb)
d2 = networkDevice(2, "HELLOUNIVERSE", env, eb, direction=-1, y=50)

env.run(until=70)