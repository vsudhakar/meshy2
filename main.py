# Main Simulation File

# Used libraries
import simpy

# Local modules
from networkDevice import *
from eventBuffer import *

# Simulation
n = 20
dim = (100, 100)

env = simpy.Environment()
eb = eventBuffer(env, n, dim)

devices = []

# Populate device array
# for i in range(0, 10):
#     devices.append(networkDevice(i, "HelloWorld", env, eb))
#
# for i in range(10, 20):
#     devices.append(networkDevice(i, "HelloWorld", env, eb, direction=-1, y = 50))
for i in range(0, n):
    devices.append(networkDevice(i, "HelloWorld", env, eb))

env.run(until=700)