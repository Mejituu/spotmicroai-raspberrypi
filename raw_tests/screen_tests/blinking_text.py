import time
import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd()

while True:
    mylcd.lcd_display_string(u"Quina marcha", 1)
    mylcd.lcd_display_string(u"porta...", 2)
    time.sleep(1)
    mylcd.lcd_clear()
    mylcd.lcd_display_string(u"-----JuanLu-----", 2)
    time.sleep(1)
    mylcd.lcd_clear()
    time.sleep(1)

