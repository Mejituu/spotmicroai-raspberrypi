#!/home/pi/spotmicro/venv/bin/python3 -u

from __future__ import division
import RPi_LCD_16x2_I2C_driver
import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685

servo_pin_a = 17

pwm = Adafruit_PCA9685.PCA9685()
servo_min = 100  # Min pulse length out of 4096
servo_max = 510  # Max pulse length out of 4096

pwm.set_pwm_freq(50)

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin_a, GPIO.OUT)

left_leg = GPIO.PWM(servo_pin_a, 50) # GPIO 17 for PWM with 50Hz

try:

    while True:
        dc_left = 2.5
        left_leg.start(dc_left)

        pwm.set_pwm(0, 0, servo_min)

        time.sleep(3)

        dc_left = 12.5
        left_leg.ChangeDutyCycle(dc_left)

        pwm.set_pwm(0, 0, servo_max)

        time.sleep(3)

finally:
    left_leg.stop()
    GPIO.cleanup()
