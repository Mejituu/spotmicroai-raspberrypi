import RPi_LCD_16x2_I2C_driver
import time


mylcd = RPi_LCD_16x2_I2C_driver.lcd()

while True:
    mylcd.lcd_display_string(u"Hello world!")
    time.sleep(1)
    mylcd.lcd_clear()
    time.sleep(1)
    