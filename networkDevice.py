# NetworkDevice Process File

# Used libraries


#Main node class

class networkDevice:
    def __init__(self, deviceID, verificationCode, env, eventBuffer, direction=1, x=0, y=0):
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

        # Neighboring device array
        self.neighbors = []

        # Simpy init methods
        self.action = env.process(self.run())

    def run(self):
        while True:
            # Test simulation
            self.y += self.direction
            print "X is %d" % self.x
            print "Y is %d" % self.y
            loc = (self.id, self.x, self.y)
            self.eventBuffer.updateLocation(loc)

            self.search()

            print "Neighbors"
            for i in self.neighbors:
                print i
            print "---------"

            yield self.env.timeout(2)

    def search(self):
        # Clear previous neighbors
        self.neighbors = []

        for i in self.eventBuffer.getLocations():
            x, y = i[1], i[2]
            radius = 2
            distance = (((x-self.x)**2)+((y-self.y)**2))**0.5
            if distance <= radius and i[0] != self.id:
                self.neighbors.append(i[0])


