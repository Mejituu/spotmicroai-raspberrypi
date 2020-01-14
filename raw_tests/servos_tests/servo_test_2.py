# https://learn.adafruit.com/16-channel-pwm-servo-driver/library-reference

# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("servo")
parser.add_argument("min")
parser.add_argument("max")
args = parser.parse_args()
print(args)

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
x = int(args.servo)
servo_min = int(args.min)  # Min pulse length out of 4096
servo_max = int(args.max)  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel ' + str(x) + ' from min ' + str(servo_min) + ' to max ' + str(servo_max) + ', press Ctrl-C to quit...')

#while True:
    # Move servo on channel O between extremes.

def move_servo(x):
    while True:
        pwm.set_pwm(x, 0, servo_min)
        time.sleep(2)
        pwm.set_pwm(x, 0, servo_max)
        time.sleep(2)

# Posición recogida
pwm.set_pwm(0, 0, 275) # hombro
pwm.set_pwm(1, 0, 550) # pie
pwm.set_pwm(2, 0, 87) # pierna

pwm.set_pwm(4, 0, 475) # hombro
pwm.set_pwm(5, 0, 88) # pie
pwm.set_pwm(6, 0, 658) # pierna

pwm.set_pwm(8, 0, 400)
pwm.set_pwm(9, 0, 88)
pwm.set_pwm(10, 0, 656)

pwm.set_pwm(12, 0, 150) # hombro
pwm.set_pwm(13, 0, 657) # pie
pwm.set_pwm(14, 0, 88) # pierna

#set_servo_pulse(10, servo_min)
move_servo(x)
