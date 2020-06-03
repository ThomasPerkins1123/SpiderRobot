import RPi.GPIO as GPIO

import config

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

for servoPIN in config.legs.values():
    p = GPIO.PWM(servoPIN, 50)
    p.start(2.5)
    p.stop()
    GPIO.cleanup()
