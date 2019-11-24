import sys
import time
from gpiozero import AngularServo
import numpy

print("Left: " + sys.argv[1])
print("Right:" + sys.argv[2])

leftArm = int(sys.argv[1])
rightArm = int(sys.argv[2])

min = -90
max = 180

leftServo = AngularServo(leftArm, min_angle=min, max_angle=max)
rightServo = AngularServo(rightArm, min_angle=min, max_angle=max)

while True:

    for x in range(min, 180, 1):
        print(x)

        # leftServo.angle = 0 - x
        rightServo.angle = x

        time.sleep(0.005)


time.sleep(1)

leftServo.detach()
rightServo.detach()

