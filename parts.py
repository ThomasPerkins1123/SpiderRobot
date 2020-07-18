import time
from config import legPins
import pigpio


pi = pigpio.pi()

def getOposite(string):
    if string == "front":
        return "back"
    if string == "back":
        return "front"
    if string == "left":
        return "right"
    if string == "right":
        return "left"

def getOpositeLeg(leg):
    return getOposite(leg.split("_")[0]) + "_"  + getOposite(leg.split("_")[1])

class Spider:
    def __init__(self):
        self.front_right = Leg([legPins["fr-1"], legPins["fr-2"], legPins["fr-3"]], True, True)
        self.front_left = Leg([legPins["fl-1"], legPins["fl-2"], legPins["fl-3"]], True, False)
        self.back_right = Leg([legPins["br-1"], legPins["br-2"], legPins["br-3"]], False, True)
        self.back_left = Leg([legPins["bl-1"], legPins["bl-2"], legPins["bl-3"]], False, False)
        self.legs = {"front_right": self.front_right, "front_left": self.front_left, "back_right": self.back_right, "back_left": self.back_left}

    def wave(self, leg):
        opositeLeg = getOpositeLeg(leg) 
        self.legs[opositeLeg].knee.goTo(130)
        self.legs[opositeLeg].foot.goTo(70)
        self.legs[leg].knee.goTo(50)
        time.sleep(0.2)
        self.legs[leg].wave()
        self.legs[opositeLeg].foot.goTo(90)
        time.sleep(0.1)
        self.legs[opositeLeg].knee.goTo(90)
    
    def bounce(self, count):
        for i in range(0, count):
            for leg in self.legs.values():
                leg.knee.goTo(0)
                leg.foot.goTo(110)
            time.sleep(0.5)
            for leg in self.legs.values():
                leg.knee.goTo(110)
                leg.foot.goTo(70)
            time.sleep(0.5)

        for leg in self.legs.values():
            leg.knee.goTo(90)
            leg.foot.goTo(90)
class Leg:
    def __init__(self, pins, front, right):
        self.hip = Joint(pins[0], [600, 500, 500], front ^ right)
        self.knee = Joint(pins[1], [300, 1000], not (front ^ right))
        self.foot = Joint(pins[2], [700, 900, 100], front ^ right)

    def wave(self):
        self.knee.goMax()
        self.foot.goMin()
        time.sleep(0.5)
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
        self.flipped = flipped
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

    def printStats(self):
        print("Min: " + str(self.min))
        print("Max: " + str(self.max))
        print("Center: " + str(self.center))

    def goTo(self, angle):
        angle = angle / 180
        angle -= 0.5
        if self.flipped:
            angle = angle * -2000
        else:
            angle = angle * 2000
        angle += self.center
        if angle < self.max and self.flipped:
            angle = self.max
        if angle > self.min and self.flipped:
            angle = self.min
        if angle > self.max and not self.flipped:
            angle = self.max
        if angle < self.min and not self.flipped:
            angle = self.min
        pi.set_servo_pulsewidth(self.pinNumber, angle)
