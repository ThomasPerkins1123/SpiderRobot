import time
import pigpio


pi = pigpio.pi()

class Leg:
    def __init__(self, pins):
        self.hip = Joint(pins[0], [1200, 1800])
        self.knee = Joint(pins[1], [1200, 1800])
        self.foot = Joint(pins[2], [1200, 1800])

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
    def __init__(self, pinNumber, rangeOfMotion):
        self.pinNumber = pinNumber
        pi.set_mode(pinNumber, pigpio.OUTPUT)
        self.min = rangeOfMotion[0]
        self.max = rangeOfMotion[1]

    def goMiddle(self):
        pi.set_servo_pulsewidth(self.pinNumber, 1500)
    
    def goMax(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.max)

    def goMin(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.min)

