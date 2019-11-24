import sys
import time
from gpiozero import AngularServo


class MotorFunction:
    def __init__(self):

        self.leftArmPin = 4
        self.leftArmMin = -180
        self.leftArmMax = -100

        self.rightArmPin = 17
        self.rightArmMin = -180
        self.rightArmMax = 0

        self.swivelPin = 27
        self.swivelArmMin = -180
        self.swivelArmMax = 180

        self.leftServo = AngularServo(self.leftArmPin, min_angle=-180, max_angle=180)
        self.rightServo = AngularServo(self.rightArmPin, min_angle=-180, max_angle=180)
        self.swivelServo = AngularServo(self.swivelPin, min_angle=-180, max_angle=180)

        self.increment = 10

    def move(self, startFraction, endFraction, servo, min, max, duration):
        startPos = int((max - min) * startFraction + min)
        endPos = int((max - min) * endFraction + min)
        delay = duration / ((endPos - startPos) / self.increment)

        # print("Start: " + startPos + " End: " + endPos + " Delay:" + delay)
        print("Delay:")
        print(delay)
        for x in range(startPos, endPos, self.increment):
            print(x)
            time.sleep(delay)
            servo.angle = x

    def moveSwivel(self, start, end, time):
        motorControl.move(
            start, end, self.swivelServo, self.swivelArmMin, self.swivelArmMax, time,
        )

    def moveLeftArm(self, start, end, time):
        motorControl.move(
            start, end, self.leftServo, self.leftArmMin, self.leftArmMax, time,
        )

    def moveRightArm(self, start, end, time):
        motorControl.move(
            start, end, self.rightServo, self.rightArmMin, self.rightArmMax, time,
        )


motorControl = MotorFunction()
while True:

    # motorControl.moveLeftArm(0, 1, 0.5)
    # time.sleep(1

    motorControl.moveLeftArm(0, 1, 0.6)
    motorControl.moveRightArm(0, 1, 0.6)
    time.sleep(1)
    motorControl.moveSwivel(0, 1, 0.6)
    time.sleep(1)
