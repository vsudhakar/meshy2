# NetworkDevice Process File

# Used libraries


#Main node class

class networkDevice:
    def __init__(self, deviceID, verificationCode, env, eventBuffer, locationProvider, direction=1, x=0, y=0):
        # Parameters
        # deviceID - Number assigned by simulation in place of device/user identification string
        # verificationCode - String used to ensure successful decryption of message
        # env - Simpy simulation environment object
        self.id = deviceID
        self.verificationCode = verificationCode
        self.env = env
        self.eventBuffer = eventBuffer

        # Define starting coordinates (cartesian)
        self.x = x      # x coordinate
        self.y = y      # y coordinate

        # TEST ONLY - DEFINE DIRECTION
        self.direction = direction

        # Location provider object
        self.locProv = locationProvider

        # Neighboring device array
        self.neighbors = []

        # Simpy init methods
        self.action = env.process(self.run)


    @property
    def run(self):
        while True:
            # Test simulation
            #self.y += self.direction
            #print "X is %d" % self.x
            #print "Y is %d" % self.y
            #loc = (self.id, self.x, self.y)


            # self.search()
            #
            # if len(self.neighbors) > 0:
            #     print str(self.id) + " Neighbors @ " + str(self.env.now)
            #     for i in self.neighbors:
            #         print i
            #     print "---------"
            #
            # if self.id == self.eventBuffer.numOfDevices-1:
            #     print "Device Id: " + str(self.id)
            #     print "Time: " + str(self.env.now)
            # else:
            #     print "WOGAY SIR: " + str(self.eventBuffer.numOfDevices-self.id-1) + " to go!"

            self.coordinates = self.locProv.getCoordinates(self.loc)

            print "Current coordinates of device " + str(self.id) + " are " + str(self.coordinates)

            yield self.env.timeout(1)

    # @property
    # def run(self):
    #     while True:
    #         yield self.env.timeout(i)


    def search(self):
        # Clear previous neighbors
        self.neighbors = []

        for i in self.eventBuffer.getLocations():
            x, y = i[1], i[2]
            radius = 2
            distance = (((x-self.x)**2)+((y-self.y)**2))**0.5

            if distance <= radius and i[0] != self.id:
                self.neighbors.append(i[0])

        # Call flush if last device
        if self.id == self.eventBuffer.numOfDevices-1:
            self.eventBuffer.next()

        # loc = (self.id, self.x, self.y)
        #
        # self.eventBuffer.updateLocation(loc)

        mobilityLoc = self.eventBuffer.getThisLocation(self.id)
        loc = (self.id, mobilityLoc[0], mobilityLoc[1])
        self.eventBuffer.updateLocation(loc)

    def setLoc(self, index):
        self.loc = index
