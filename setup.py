import pigpio

import config

pi = pigpio.pi()

if __name__ == "__main__":
    while True:
        servoPIN = int(input("Enter a servo pin:"))
        pi.set_mode(servoPIN, pigpio.OUTPUT)
        pi.set_servo_pulsewidth(servoPIN, 1800)
        time.sleep(0.5)
        pi.set_servo_pulsewidth(servoPIN, 1500)
        time.sleep(0.5)
        pi.set_servo_pulsewidth(servoPIN, 1200)
