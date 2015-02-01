# Main Simulation File

# Used libraries
import simpy

# Local modules
from networkDevice import *
from eventBuffer import *
from locationProvider import *

# Simulation
n = 28572/4
dim = (6896/4, 6896/4)

env = simpy.Environment()
eb = eventBuffer(env, n, dim)

devices = []

locProv = locationProvider(env, n, dim, devices, div=20)

# Populate device array
# for i in range(0, 10):
#     devices.append(networkDevice(i, "HelloWorld", env, eb))
#
# for i in range(10, 20):
#     devices.append(networkDevice(i, "HelloWorld", env, eb, direction=-1, y = 50))
for i in range(0, n):
    print "Wogay?"
    devices.append(networkDevice(i, "HelloWorld", env, eb, locProv))
    print "Wogay sir: " + str(n - i) + " left."

locProv.setDevices(devices)

env.run(until=60)