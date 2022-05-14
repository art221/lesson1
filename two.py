class Monitor:
    displayResolution = 0
    screenSize = 0
    rate = 0
    def __init__(self,px,dm,Hz):
        print("Create nem Monitor")
        self.displayResolution = px
        self.screenSize = dm
        self.rate = Hz


lg = Monitor(1500,500,1000)
philips = Monitor(1250,400,900)
print("--==LG==--")
print("display Resolution:", lg.displayResolution)
print("screenSize", lg.screenSize)
print("rate", lg.rate)
print("--===PHILIPS===--")
print("--==LG==--")
print("display Resolution:", philips.displayResolution)
print("screenSize", philips.screenSize)
print("rate", philips.rate)