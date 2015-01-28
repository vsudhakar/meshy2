# eventBuffer class for simulation

class eventBuffer:
    def __init__(self, env):
        self.deviceLocation = []

        # Simpy init methods
        self.env = env
        self.action = env.process(self.run())

    def updateLocation(self, loc):
        # loc -> (deviceID, x, y)
        self.deviceLocation.append(loc)

    def getLocations(self):
        return self.deviceLocation

    def run(self):
        while True:
            self.deviceLocation = []
            yield self.env.timeout(1)