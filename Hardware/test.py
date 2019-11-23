import sys
import RPi.GPIO as GPIO
import time

print(sys.argv[1])
print(sys.argv[2])

servoPIN = int(sys.argv[1])
angle = float(sys.argv[2])/(180)+1
print(servoPIN)
print(angle)

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

p.ChangeDutyCycle(angle)
time.sleep(1)

p.stop()
GPIO.cleanup()
