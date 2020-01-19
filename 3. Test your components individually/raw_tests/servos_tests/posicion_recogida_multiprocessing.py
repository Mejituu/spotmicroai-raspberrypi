from __future__ import division
from multiprocessing import Process
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

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

# Posición recogida

p0 = Process(target=pwm.set_pwm(0, 0, 275))
p0.start()
p1 = Process(target=pwm.set_pwm(1, 0, 87))
p1.start()
p2 = Process(target=pwm.set_pwm(2, 0, 657))
p2.start()

p4 = Process(target=pwm.set_pwm(4, 0, 475))
p4.start()
p5 = Process(target=pwm.set_pwm(5, 0, 658))
p5.start()
p6 = Process(target=pwm.set_pwm(6, 0, 87))
p6.start()

p8 = Process(target=pwm.set_pwm(8, 0, 400))
p8.start()
p9 = Process(target=pwm.set_pwm(9, 0, 658))
p9.start()
p10 = Process(target=pwm.set_pwm(10, 0, 88))
p10.start()

p12 = Process(target=pwm.set_pwm(12, 0, 150))
p12.start()
p13 = Process(target=pwm.set_pwm(13, 0, 87))
p13.start()
p14 = Process(target=pwm.set_pwm(14, 0, 657))
p14.start()

p0.join()
p1.join()
p2.join()

p4.join()
p5.join()
p6.join()

p8.join()
p9.join()
p10.join()

p12.join()
p13.join()
p14.join()
