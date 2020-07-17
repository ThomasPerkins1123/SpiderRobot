import time
import pigpio


pi = pigpio.pi()

class Leg:
    def __init__(self, pins, front, right):
        self.hip = Joint(pins[0], [1300, 2200, 400], not front)
        self.knee = Joint(pins[1], [600, 1800], right)
        self.foot = Joint(pins[2], [800, 2500], not front)

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
            if not flipped:
                self.center += rangeOfMotion[2]
            else:
                self.center -= rangeOfMotion[2]
        self.goMiddle()

    def goMiddle(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.center)
    
    def goMax(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.max)

    def goMin(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.min)

