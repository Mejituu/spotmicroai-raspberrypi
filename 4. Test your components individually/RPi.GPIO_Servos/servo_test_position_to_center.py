
#!/home/pi/spotmicro/venv/bin/python3 -u

import RPi_LCD_16x2_I2C_driver
import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz

mylcd = RPi_LCD_16x2_I2C_driver.lcd()

p.start(7.5)

try:
    while True:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("DutyCycle 2.5", 2)
        mylcd.lcd_display_string("Min 0 deg", 1)
        p.ChangeDutyCycle(2.5)  # turn towards 0 degree
        time.sleep(4)

        mylcd.lcd_clear()
        mylcd.lcd_display_string("DutyCycle 7.5", 2)
        mylcd.lcd_display_string("Middle 90 deg", 1)
        p.ChangeDutyCycle(7.5)  # turn towards 90 degree
        time.sleep(4)

        mylcd.lcd_clear()
        mylcd.lcd_display_string("DutyCycle 12.5", 2)
        mylcd.lcd_display_string("Max 180 deg", 1)
        p.ChangeDutyCycle(12.5) # turn towards 180 degree
        time.sleep(4)

        mylcd.lcd_clear()
        mylcd.lcd_display_string("DutyCycle 7.5", 2)
        mylcd.lcd_display_string("Middle 90 deg", 1)
        p.ChangeDutyCycle(7.5)  # turn towards 90 degree
        time.sleep(4)


except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
