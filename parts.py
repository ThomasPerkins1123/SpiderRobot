import time
from config import legPins
import pigpio


pi = pigpio.pi()

class Spider:
    def __init__(self):
        self.frontRight = Leg([legPins["fr-1"], legPins["fr-2"], legPins["fr-3"]], True, True)
        self.frontLeft = Leg([legPins["fl-1"], legPins["fl-2"], legPins["fl-3"]], True, False)
        self.backRight = Leg([legPins["br-1"], legPins["br-2"], legPins["br-3"]], False, True)
        self.backLeft = Leg([legPins["bl-1"], legPins["bl-2"], legPins["bl-3"]], False, False)

class Leg:
    def __init__(self, pins, front, right):
        self.hip = Joint(pins[0], [200, 500, 500], front ^ right)
        self.knee = Joint(pins[1], [300, 1000], not (front ^ right))
        self.foot = Joint(pins[2], [700, 900, 100], front ^ right)

    def wave(self):
        self.hip.goMiddle()
        self.knee.goMiddle()
        self.foot.goMiddle()
       
        time.sleep(1)
        self.knee.goMax()
        self.foot.goMin()
        time.sleep(1)
        self.hip.goMax()
        time.sleep(0.2)
        self.hip.goMin()
        time.sleep(0.2)
        self.hip.goMiddle()
        time.sleep(0.5)

        self.hip.goMiddle()
        self.knee.goMiddle()
        self.foot.goMiddle()


class Joint:
    def __init__(self, pinNumber, rangeOfMotion, flipped):
        self.pinNumber = pinNumber
        pi.set_mode(pinNumber, pigpio.OUTPUT)
        self.center = 1500
        if len(rangeOfMotion) > 2:
            if not flipped:
                self.center += rangeOfMotion[2]
            else:
                self.center -= rangeOfMotion[2]

        self.min = self.center
        self.max = self.center

        if not flipped:
            self.min -= rangeOfMotion[0]
            self.max += rangeOfMotion[1]
        else:
            self.min += rangeOfMotion[0]
            self.max -= rangeOfMotion[1]
        self.goMiddle()

    def goMiddle(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.center)
    
    def goMax(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.max)

    def goMin(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.min)

