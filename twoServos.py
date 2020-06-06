import RPi.GPIO as GPIO
import time

servoPIN = 14
servoPIN2 = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)


p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
a = GPIO.PWM(servoPIN2, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
a.start(2.5) # Initialization
try:
  while True:     
    p.ChangeDutyCycle(5)
    a.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    a.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    a.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    a.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    a.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    a.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    a.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    a.ChangeDutyCycle(2.5)
    time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  a.stop()
  GPIO.cleanup()
