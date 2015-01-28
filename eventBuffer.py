# eventBuffer class for simulation

class eventBuffer:
    def __init__(self, env, numOfDevices):
        self.deviceLocation = []
        self.numOfDevices = numOfDevices

        # Simpy init methods
        self.env = env
        #self.action = env.process(self.run())

    def updateLocation(self, loc):
        # loc -> (deviceID, x, y)
        self.deviceLocation.append(loc)

    def getLocations(self):
        return self.deviceLocation

    def next(self):
        self.deviceLocation = []
        #print "Event buffer cleared"

    def run(self):
        while True:
            self.deviceLocation = []
            print "Event buffer cleared"
            yield self.env.timeout(1)