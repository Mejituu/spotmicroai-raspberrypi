#!/usr/bin/env python3

from spotmicropi.output.screen_lcd16x2_i2c.screen_lcd16x2_i2c import ScreenLCD16x2I2c
import spotmicropi.utilities.log as logger

log = logger.setup_logger('IntegrationTest_ScreenLCD16x2I2c')

if __name__ == '__main__':
    i2c_address = 41

    screen = ScreenLCD16x2I2c(i2c_address)

    screen.clear()
    screen.write_first_line()
    screen.write_second_line()
    screen.turn_off()
    screen.turn_on()
