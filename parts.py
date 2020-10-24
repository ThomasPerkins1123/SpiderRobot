import time
from config import leg_pins
import pigpio


pi = pigpio.pi()


def get_opposite(string):
    if string == "front":
        return "back"
    if string == "back":
        return "front"
    if string == "left":
        return "right"
    if string == "right":
        return "left"


def get_opposite_leg(leg):
    return get_opposite(leg.split("_")[0]) + "_" + get_opposite(leg.split("_")[1])


class Spider:
    def __init__(self):
        self.front_right = Leg([leg_pins["fr-1"], leg_pins["fr-2"], leg_pins["fr-3"]], True, True)
        self.front_left = Leg([leg_pins["fl-1"], leg_pins["fl-2"], leg_pins["fl-3"]], True, False)
        self.back_right = Leg([leg_pins["br-1"], leg_pins["br-2"], leg_pins["br-3"]], False, True)
        self.back_left = Leg([leg_pins["bl-1"], leg_pins["bl-2"], leg_pins["bl-3"]], False, False)
        self.legs = {"front_right": self.front_right, "front_left": self.front_left, "back_right": self.back_right, "back_left": self.back_left}

    def walk(self):
        self.move_leg_forward("back_left")
        self.move_leg_forward("back_right")
        self.back_right.knee.go_to(100)
        self.back_left.knee.go_to(100)
        time.sleep(0.3)
        self.front_right.hip.go_min()
        self.front_left.hip.go_min()
        self.back_right.hip.go_middle()
        self.back_left.hip.go_middle()
        self.move_leg_back("front_right")
        self.move_leg_back("front_left")
        self.back_right.knee.go_to(90)
        self.back_left.knee.go_to(90)

    def move_leg_back(self, leg):
        self.raise_leg(leg)
        self.legs[leg].hip.go_middle()
        self.legs[leg].knee.go_middle()
        self.legs[leg].foot.go_middle()

    def move_leg_forward(self, leg):
        self.raise_leg(leg)
        self.legs[leg].hip.go_to(90)
        time.sleep(0.2)
        self.legs[leg].knee.go_to(120)
        self.legs[leg].foot.go_to(50)
        time.sleep(0.2)
        self.legs[leg].hip.go_to(0)
        time.sleep(0.2)
        self.legs[leg].knee.go_middle()
        self.legs[leg].foot.go_middle()
        time.sleep(0.2)
        self.legs[get_opposite_leg(leg)].knee.go_middle()
        self.legs[get_opposite_leg(leg)].foot.go_middle()

    def raise_leg(self, leg):
        opposite_leg = get_opposite_leg(leg)
        self.legs[opposite_leg].knee.go_to(130)
        self.legs[opposite_leg].foot.go_to(70)
        self.legs[leg].knee.go_to(50)

    def wave(self, leg):
        opposite_leg = get_opposite_leg(leg)
        self.raise_leg(leg)
        time.sleep(0.2)
        self.legs[leg].wave()
        self.legs[opposite_leg].foot.go_to(90)
        time.sleep(0.1)
        self.legs[opposite_leg].knee.go_to(90)

    def bounce(self, count):
        for i in range(0, count):
            for leg in self.legs.values():
                leg.knee.go_to(0)
                leg.foot.go_to(110)
            time.sleep(0.5)
            for leg in self.legs.values():
                leg.knee.go_to(110)
                leg.foot.go_to(70)
            time.sleep(0.5)

        for leg in self.legs.values():
            leg.knee.go_to(90)
            leg.foot.go_to(90)


class Leg:
    def __init__(self, pins, front, right):
        self.hip = Joint(pins[0], [600, 500, 500], front ^ right)
        self.knee = Joint(pins[1], [300, 1000], not (front ^ right))
        self.foot = Joint(pins[2], [700, 900, 100], front ^ right)

    def wave(self):
        self.knee.go_max()
        self.foot.go_min()
        time.sleep(0.5)
        self.hip.go_max()
        time.sleep(0.2)
        self.hip.go_min()
        time.sleep(0.2)
        self.hip.go_middle()
        time.sleep(0.5)
        self.hip.go_middle()
        self.knee.go_middle()
        self.foot.go_middle()


class Joint:
    def __init__(self, pin_number, range_of_motion, flipped):
        self.pinNumber = pin_number
        self.flipped = flipped
        pi.set_mode(pin_number, pigpio.OUTPUT)
        self.center = 1500
        if len(range_of_motion) > 2:
            if not flipped:
                self.center += range_of_motion[2]
            else:
                self.center -= range_of_motion[2]

        self.min = self.center
        self.max = self.center

        if not flipped:
            self.min -= range_of_motion[0]
            self.max += range_of_motion[1]
        else:
            self.min += range_of_motion[0]
            self.max -= range_of_motion[1]
        self.go_middle()

    def go_middle(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.center)

    def go_max(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.max)

    def go_min(self):
        pi.set_servo_pulsewidth(self.pinNumber, self.min)

    def print_stats(self):
        print("Min: " + str(self.min))
        print("Max: " + str(self.max))
        print("Center: " + str(self.center))

    def go_to(self, angle):
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
