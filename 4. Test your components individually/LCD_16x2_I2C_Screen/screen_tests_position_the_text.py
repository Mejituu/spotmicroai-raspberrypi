import RPi_LCD_16x2_I2C_driver

mylcd = RPi_LCD_16x2_I2C_driver.lcd()

mylcd.lcd_display_string_pos("Hello World!", 2, 3)
