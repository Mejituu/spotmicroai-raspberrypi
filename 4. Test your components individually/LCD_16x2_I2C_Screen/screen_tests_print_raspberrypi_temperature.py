import RPi_LCD_16x2_I2C_driver
import os
import time

mylcd = RPi_LCD_16x2_I2C_driver.lcd()

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

while True:
        mylcd.lcd_display_string(measure_temp().rstrip(), 1)
        time.sleep(2)
