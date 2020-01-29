#!/home/pi/spotmicro/venv/bin/python3 -u

# This example moves a servo its full range (180 degrees by default) and then back.

import RPi.GPIO as GPIO

from board import SCL, SDA
import busio

import time

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# This example also relies on the Adafruit motor library available here:
# https://github.com/adafruit/Adafruit_CircuitPython_Motor
from adafruit_motor import servo

i2c = busio.I2C(SCL, SDA)

pca_rear = PCA9685(i2c, address=0x40)
pca_rear.frequency = 50

pca_front = PCA9685(i2c, address=0x42)
pca_front.frequency = 50

servo_rear_shoulder_left = servo.Servo(pca_rear.channels[0], min_pulse=352, max_pulse=2664)
servo_rear_leg_left = servo.Servo(pca_rear.channels[1], min_pulse=352, max_pulse=2664)
servo_rear_feet_left = servo.Servo(pca_rear.channels[3], min_pulse=352, max_pulse=2664)

servo_rear_shoulder_right = servo.Servo(pca_rear.channels[15], min_pulse=352, max_pulse=2664)
servo_rear_leg_right = servo.Servo(pca_rear.channels[14], min_pulse=352, max_pulse=2664)
servo_rear_feet_right = servo.Servo(pca_rear.channels[8], min_pulse=352, max_pulse=2664)

servo_front_shoulder_left = servo.Servo(pca_front.channels[11], min_pulse=352, max_pulse=2664)
servo_front_leg_left = servo.Servo(pca_front.channels[9], min_pulse=352, max_pulse=2664)
servo_front_feet_left = servo.Servo(pca_front.channels[8], min_pulse=352, max_pulse=2664)

servo_front_shoulder_right = servo.Servo(pca_front.channels[7], min_pulse=352, max_pulse=2664)
servo_front_leg_right = servo.Servo(pca_front.channels[6], min_pulse=352, max_pulse=2664)
servo_front_feet_right = servo.Servo(pca_front.channels[4], min_pulse=352, max_pulse=2664)



try:

    time.sleep(1)

    servo_rear_shoulder_left.angle = 85
    servo_rear_leg_left.angle = 75
    servo_rear_feet_left.angle = 30

    servo_rear_shoulder_right.angle = 102
    servo_rear_leg_right.angle = 120
    servo_rear_feet_right.angle = 160

    servo_front_shoulder_left.angle = 105
    servo_front_leg_left.angle = 65
    servo_front_feet_left.angle = 40

    servo_front_shoulder_right.angle = 105
    servo_front_leg_right.angle = 140
    servo_front_feet_right.angle = 165

    time.sleep(5)

finally:
    pca_rear.deinit()
    pca_front.deinit()

