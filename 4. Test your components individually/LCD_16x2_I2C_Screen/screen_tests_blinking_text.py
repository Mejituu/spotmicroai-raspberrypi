#!/home/pi/spotmicro/venv/bin/python3 -u

import RPi_LCD_16x2_I2C_driver
import time


mylcd = RPi_LCD_16x2_I2C_driver.lcd()

while True:
    mylcd.lcd_display_string(u"Hello world!", 1)
    time.sleep(1)
    mylcd.lcd_clear()
    time.sleep(1)
    