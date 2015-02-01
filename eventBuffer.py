# eventBuffer class for simulation

# Used libraries
from pymobility.models.mobility import reference_point_group

class eventBuffer:
    def __init__(self, env, numOfDevices, dim):
        # self.deviceLocation = []
        self.numOfDevices = numOfDevices
        # self.mobility = reference_point_group(self.numOfDevices, dimensions=dim, velocity=(0.1, 1.0))
        # self.locations = self.mobility.next()

        # Simpy init methods
        self.env = env
        #self.action = env.process(self.run())

    # def getThisLocation(self, id):
    #     return self.locations[id]
    #
    # def updateLocation(self, loc):
    #     # loc -> (deviceID, x, y)
    #     self.deviceLocation.append(loc)
    #
    # def getLocations(self):
    #     return self.deviceLocation

    # def next(self):
    #     self.deviceLocation = []
    #     self.locations = self.mobility.next()

    # def run(self):
    #     while True:
    #         self.deviceLocation = []
    #         print "Event buffer cleared"
    #         yield self.env.timeout(1)