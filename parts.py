import time
import pigpio


pi = pigpio.pi()

class Leg:
    def __init__(self, pins, front, right):
        self.hip = Joint(pins[0], [1000, 1600, 1300], front)
        self.knee = Joint(pins[1], [1200, 1800], right)
        self.foot = Joint(pins[2], [1200, 1800], right)

    def wave(self):
        self.hip.goMiddle()
        self.knee.goMiddle()
        self.foot.goMiddle()
       
        time.sleep(1)
        self.knee.goMax()
        self.foot.goMin()
        time.sleep(1)
        self.hip.goMax()
        time.sleep(1)
        self.hip.goMin()
        time.sleep(1)

        self.hip.goMiddle()
        self.knee.goMiddle()
        self.foot.goMiddle()


class Joint:
    def __init__(self, pinNumber, rangeOfMotion, flipped):
        self.pinNumber = pinNumber
        pi.set_mode(pinNumber, pigpio.OUTPUT)
        self.center = 1500
        if not flipped:
            self.min = rangeOfMotion[0]
            self.max = rangeOfMotion[1]
        else:    
            self.min = rangeOfMotion[1]
            self.max = rangeOfMotion[0]
        if len(rangeOfMotion) > 2:
            self.center = rangeOfMotion[2]

    def goMiddle(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.center)
    
    def goMax(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.max)

    def goMin(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.min)

