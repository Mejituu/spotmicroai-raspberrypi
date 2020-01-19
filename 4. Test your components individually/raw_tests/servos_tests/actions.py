from __future__ import division
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

pwm.set_pwm_freq(60)

# Standby position
pwm.set_pwm(0, 0, 350) # hombro
pwm.set_pwm(1, 0, 470) # pie
pwm.set_pwm(2, 0, 90) # pierna

pwm.set_pwm(4, 0, 375) # hombro
pwm.set_pwm(5, 0, 245) # pie
pwm.set_pwm(6, 0, 610) # pierna

pwm.set_pwm(8, 0, 250) # hombro
pwm.set_pwm(9, 0, 470) # pie
pwm.set_pwm(10, 0, 90) # pierna

pwm.set_pwm(12, 0, 350) # hombro
pwm.set_pwm(13, 0, 245) # pie
pwm.set_pwm(14, 0, 600) # pierna

time.sleep(5)

for i in range(2):

    # Standby position
    pwm.set_pwm(0, 0, 450) # hombro
    pwm.set_pwm(1, 0, 470) # pie
    pwm.set_pwm(2, 0, 90) # pierna

    pwm.set_pwm(4, 0, 475) # hombro
    pwm.set_pwm(5, 0, 245) # pie
    pwm.set_pwm(6, 0, 610) # pierna

    pwm.set_pwm(8, 0, 350) # hombro
    pwm.set_pwm(9, 0, 470) # pie
    pwm.set_pwm(10, 0, 90) # pierna

    pwm.set_pwm(12, 0, 450) # hombro
    pwm.set_pwm(13, 0, 245) # pie
    pwm.set_pwm(14, 0, 600) # pierna

    time.sleep(2)

    # Standby position
    pwm.set_pwm(0, 0, 250) # hombro
    pwm.set_pwm(1, 0, 470) # pie
    pwm.set_pwm(2, 0, 90) # pierna

    pwm.set_pwm(4, 0, 275) # hombro
    pwm.set_pwm(5, 0, 245) # pie
    pwm.set_pwm(6, 0, 610) # pierna

    pwm.set_pwm(8, 0, 150) # hombro
    pwm.set_pwm(9, 0, 470) # pie
    pwm.set_pwm(10, 0, 90) # pierna

    pwm.set_pwm(12, 0, 250) # hombro
    pwm.set_pwm(13, 0, 245) # pie
    pwm.set_pwm(14, 0, 600) # pierna

    time.sleep(2)

# Standby position
pwm.set_pwm(0, 0, 350) # hombro
pwm.set_pwm(1, 0, 470) # pie
pwm.set_pwm(2, 0, 90) # pierna

pwm.set_pwm(4, 0, 375) # hombro
pwm.set_pwm(5, 0, 245) # pie
pwm.set_pwm(6, 0, 610) # pierna

pwm.set_pwm(8, 0, 250) # hombro
pwm.set_pwm(9, 0, 470) # pie
pwm.set_pwm(10, 0, 90) # pierna

pwm.set_pwm(12, 0, 350) # hombro
pwm.set_pwm(13, 0, 245) # pie
pwm.set_pwm(14, 0, 600) # pierna


for i in range(2):

    # Standby position
    pwm.set_pwm(0, 0, 350) # hombro
    pwm.set_pwm(1, 0, 470) # pie
    pwm.set_pwm(2, 0, 90) # pierna

    pwm.set_pwm(4, 0, 375) # hombro
    pwm.set_pwm(5, 0, 245) # pie
    pwm.set_pwm(6, 0, 610) # pierna

    pwm.set_pwm(8, 0, 250) # hombro
    pwm.set_pwm(9, 0, 270) # pie
    pwm.set_pwm(10, 0, 390) # pierna

    pwm.set_pwm(12, 0, 350) # hombro
    pwm.set_pwm(13, 0, 445) # pie
    pwm.set_pwm(14, 0, 300) # pierna

    time.sleep(2)

    # Standby position
    pwm.set_pwm(0, 0, 350) # hombro
    pwm.set_pwm(1, 0, 370) # pie
    pwm.set_pwm(2, 0, 190) # pierna

    pwm.set_pwm(4, 0, 375) # hombro
    pwm.set_pwm(5, 0, 345) # pie
    pwm.set_pwm(6, 0, 510) # pierna

    pwm.set_pwm(8, 0, 250) # hombro
    pwm.set_pwm(9, 0, 470) # pie
    pwm.set_pwm(10, 0, 90) # pierna

    pwm.set_pwm(12, 0, 350) # hombro
    pwm.set_pwm(13, 0, 245) # pie
    pwm.set_pwm(14, 0, 600) # pierna

    time.sleep(2)
