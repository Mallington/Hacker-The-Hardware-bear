from SetPosition import MotorFunction
import sys
motorControl = MotorFunction()

for x in range(0,int(sys.argv[1])):
    motorControl.moveLeftArm(0, 1, 0.6)
    motorControl.moveRightArm(0, 1, 0.6)
    time.sleep(1)
    motorControl.moveSwivel(0, 1, 0.6)
    time.sleep(1)
    delay(x)

