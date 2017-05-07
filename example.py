#!/usr/bin/env python2

import RFM69
from RFM69registers import *
import datetime
import time

test = RFM69.RFM69(RF69_868MHZ, 1, 1, True)
print "class initialized"
print "Performing rcCalibration"
test.rcCalibration()
print "setting high power"
test.setHighPower(True)
print "Checking temperature"
print test.readTemperature(0)
print "setting encryption"
test.encrypt("kekusmaximus1997")
print "sending blah to 2"
while True:
    if test.sendWithRetry(2, "blah", 3, 20):
        print "ack recieved"
        time.sleep(1)
print "shutting down"
test.shutdown()
