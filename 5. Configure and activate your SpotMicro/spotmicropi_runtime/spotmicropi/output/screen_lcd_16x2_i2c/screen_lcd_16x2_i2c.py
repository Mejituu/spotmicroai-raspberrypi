import time

import spotmicropi.utilities.log as logger
from spotmicropi.output.screen_lcd_16x2_i2c import LCD_16x2_I2C_driver

log = logger.get_default_logger()


class ScreenLCD16x2I2C:

    def __init__(self, events_queue):
        log.info('Activating screen LCD_16x2_I2C at the default i2c address: ' + str(LCD_16x2_I2C_driver.ADDRESS))
        self.screen = LCD_16x2_I2C_driver.lcd()

        self._events_queue = events_queue
        self.do_process_events_from_queue()

    def do_process_events_from_queue(self):
        while True:
            event = self._events_queue.get()

            if event.startswith('screen'):
                if event.endswith('clear'):
                    self.clear()
                if event.endswith('write_first_line'):
                    self.write_first_line()
                if event.endswith('write_second_line'):
                    self.write_second_line()
                if event.endswith('turn_off'):
                    self.turn_off()
                if event.endswith('turn_on'):
                    self.turn_on()

            time.sleep(1 / 3)

    def clear(self):
        self.screen.lcd_clear()
        print('clear')

    def write_first_line(self):
        self.screen.lcd_display_string('TEXT', 1)
        print('write_first_line')

    def write_second_line(self):
        self.screen.lcd_display_string('TEXT', 2)
        print('write_second_line')

    def turn_off(self):
        print('turn_off')

    def turn_on(self):
        print('turn_on')
