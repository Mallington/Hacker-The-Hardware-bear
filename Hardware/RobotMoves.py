from SetPosition import MotorFunction
import sys
import time

class Moves:
    def __init__(self):
        self.motorControl = MotorFunction()

    def dance(self, repeats):
        for x in range(0,repeats,1):
            self.motorControl.moveSwivel(0, 1, 1)
            self.motorControl.moveRightArm(1, 1, 1)

            self.motorControl.moveSwivel(0.5, 1, 1)
            self.motorControl.moveRightArm(0, 1, 1)
            self.motorControl.moveLeftArm(0, 1, 1)

            self.motorControl.moveRightArm(1, 1, 3)
            self.motorControl.moveLeftArm(1, 1, 3)
            time.sleep(1)

    def clear(self):
        self.motorControl.clear()

