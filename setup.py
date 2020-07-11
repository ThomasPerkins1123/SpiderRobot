import os
import pigpio

import config

pi = pigpio.pi()

def centerServos():
    for servoPIN in config.legs.values():
        if servoPIN != 0:
            print(servoPIN)
            pi.set_mode(servoPIN, pigpio.OUTPUT)
            pi.set_servo_pulsewidth(servoPIN, 1500)


if __name__ == "__main__":
    centerServos()
