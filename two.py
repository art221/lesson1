class Monitor:
    displayResolution = 0
    screenSize = 0
    rate = 0
    def __init__(self,px,dm,Hz):
        print("Create nem Monitor")
        self.displayResolution = px
        self.screenSize = dm
        self.rate = Hz
    def printInfo(self,name):
        print(f"{name:^12}")
        print("display Resolution:", self.displayResolution)
        print("screenSize", self.screenSize)
        print("rate", self.rate)


lg = Monitor(1500,500,1000)
philips = Monitor(1250,400,900)
lg.printInfo("LG")
philips.printInfo("PHILIPS")