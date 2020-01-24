import RPi_LCD_16x2_I2C_driver
import time

mylcd = RPi_LCD_16x2_I2C_driver.lcd()


while True:
    mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1)
    
    mylcd.lcd_display_string("Date: %s" %time.strftime("%m/%d/%Y"), 2)
    