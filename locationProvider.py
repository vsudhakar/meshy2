#locationProvider class

# Used libraries
from pymobility.models.mobility import reference_point_group

class locationProvider:
    def __init__(self, env, numOfDevices, dim, devices, div = 15):
        self.numOfDevices = numOfDevices

        # Simpy init methods
        self.env = env
        self.action = env.process(self.run())

        # Split dimension into grid
        self.dim = dim
        self.div = div

        fracWidth = dim[0] / div
        fracHeight = dim[1] / div

        self.devices = devices

        self.xGrid = []

        for i in range(div):
            self.xGrid.append([None] * div)

        # Create random waypoint object and grab locations
        self.mobility = reference_point_group(self.numOfDevices, dimensions=dim, velocity=(0.1, 1.0))
        locations = self.mobility.next()
        # print len(self.devices)
        # print len(locations)
        # self.next()

    def setDevices(self, devices):
        self.devices = devices

    def next(self):
        locations = self.mobility.next()

        for i in range(len(locations)):
            # print int(locations[i][0])
            #
            # print "Size of grid is " + str(len(self.xGrid))

            # X grid index
            xIndex = int(self.dim[0] // locations[i][0])
            # Y grid index
            yIndex = int(self.dim[1] // locations[i][0])

            self.devices[i].setLoc((xIndex, yIndex))

            self.xGrid[xIndex][yIndex] = locations[i]
            #
            # print "Coordinates are " + str((xIndex, yIndex))
            #
            # print "Location is " + str(self.xGrid[xIndex][yIndex])

    def getCoordinates(self, index):
        print self.xGrid[index[0]][index[1]]
        raw_input()
        return self.xGrid[index[0]][index[1]]

    def run(self):
        while True:
            print "Refreshing coordinates"
            raw_input("Hit Enter to continue")
            self.next()
            yield self.env.timeout(self.numOfDevices)