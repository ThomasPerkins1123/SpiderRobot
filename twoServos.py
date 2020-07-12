import pigpio

import time

servoPIN = 14
servoPIN2 = 15
pi = pigpio.pi()

pi.set_mode(servoPIN, pigpio.OUTPUT)
pi.set_mode(servoPIN2, pigpio.OUTPUT)

while True:     
    pi.set_servo_pulsewidth(servoPIN, 1500)
    pi.set_servo_pulsewidth(servoPIN2, 1500)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(servoPIN, 1800)
    pi.set_servo_pulsewidth(servoPIN2, 1800)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(servoPIN, 2100)
    pi.set_servo_pulsewidth(servoPIN2, 2100)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(servoPIN, 1800)
    pi.set_servo_pulsewidth(servoPIN2, 1800)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(servoPIN, 1500)
    pi.set_servo_pulsewidth(servoPIN2, 1500)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(servoPIN, 1300)
    pi.set_servo_pulsewidth(servoPIN2, 1300)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(servoPIN, 1100)
    pi.set_servo_pulsewidth(servoPIN2,1100)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(servoPIN, 1300)
    pi.set_servo_pulsewidth(servoPIN2, 1300)
    time.sleep(0.5)
