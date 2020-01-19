import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)


for i in range(6):

    kit.continuous_servo[i].throttle = -1
    time.sleep(0.5)
    kit.continuous_servo[i].throttle = 0
    time.sleep(0.5)
