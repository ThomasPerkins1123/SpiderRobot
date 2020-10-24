import pigpio

import config

pi = pigpio.pi()

if __name__ == "__main__":
    while True:
        servoPIN = input("Enter a servo pin:")
        pi.set_mode(servoPIN, pigpio.OUTPUT)
        pi.set_servo_pulsewidth(servoPIN, 1800)
        pi.set_servo_pulsewidth(servoPIN, 1500)
        pi.set_servo_pulsewidth(servoPIN, 1200)
