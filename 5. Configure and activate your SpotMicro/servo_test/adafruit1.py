# Example based from https://github.com/adafruit/Adafruit_CircuitPython_PCA9685/blob/master/examples/pca9685_servo.py
# Servo library used to simplify: https://github.com/adafruit/Adafruit_CircuitPython_Motor/blob/master/adafruit_motor/servo.py
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import time

i2c = busio.I2C(SCL, SDA)

# reference_clock_speed from: https://github.com/adafruit/Adafruit_CircuitPython_PCA9685/blob/master/examples/pca9685_calibration.py
pca = PCA9685(i2c, address=0x40, reference_clock_speed=25000000)
pca.frequency = 50

# To get the full range of the servo you will likely need to adjust the min_pulse and max_pulse to
# match the stall points of the servo.

# The pulse range is 1000 - 2000 by default.
servo_0 = servo.Servo(pca.channels[0])
servo_0.set_pulse_width_range(min_pulse=500, max_pulse=2500)

# Move by angle

servo_0.angle = 180
time.sleep(2)

for i in range(180):
    servo_0.angle = i
    time.sleep(0.01)

for i in range(180):
    servo_0.angle = 180 - i
    time.sleep(0.01)

servo_0.angle = 180
time.sleep(3)

servo_0.angle = 90
time.sleep(3)

servo_0.angle = 0
time.sleep(3)

# You can also specify the movement fractionally.
# Pulse width expressed as fraction between 0.0 (`min_pulse`) and 1.0 (`max_pulse`).
fraction = 0.0
while fraction < 1.0:
    servo_0.fraction = fraction
    fraction += 0.01
    time.sleep(0.01)

servo_0.fraction = 0
time.sleep(3)

servo_0.fraction = 0.5
time.sleep(3)

servo_0.fraction = 1
time.sleep(3)

pca.deinit()
