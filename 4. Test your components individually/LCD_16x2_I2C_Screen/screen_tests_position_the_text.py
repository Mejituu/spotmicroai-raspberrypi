import RPi_LCD_16x2_I2C_driver
from time import *

mylcd = RPi_LCD_16x2_I2C_driver.lcd()

mylcd.lcd_display_string("Hello World!", 2, 3)
