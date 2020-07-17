import pigpio

pi = pigpio.pi()

class Leg:
    def __init__(self):
        print("Setting up leg")

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

