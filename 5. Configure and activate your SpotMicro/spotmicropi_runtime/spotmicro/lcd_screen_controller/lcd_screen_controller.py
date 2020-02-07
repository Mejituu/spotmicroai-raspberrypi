import time
import signal
import queue
from spotmicro.utilities.log import Logger
from spotmicro.lcd_screen_controller import LCD_16x2_I2C_driver

log = Logger().setup_logger('LCD Screen controller')


class LCDScreenController:

    def __init__(self, communication_queues):
        try:

            log.info('Starting controller...')

            signal.signal(signal.SIGINT, self.exit_gracefully)
            signal.signal(signal.SIGTERM, self.exit_gracefully)

            self.screen = LCD_16x2_I2C_driver.lcd()

            self._lcd_screen_queue = communication_queues['lcd_screen_controller']

            self.line_1 = 'SpotMicro'
            self.line_2 = ''

            self.previous_line_1 = ''
            self.previous_line_2 = ''

            self.clear()
            self.turn_on()
            self.write_lines()

            log.info('Started')

        except Exception as e:
            log.error('LCD Screen problem detected', e)

    def exit_gracefully(self, signum, frame):
        self.clear()
        self.turn_off()
        log.info('Terminated')
        exit(0)

    def do_process_events_from_queue(self):

        try:
            while True:
                event = self._lcd_screen_queue.get()

                if event.startswith('Line1 '):
                    self.line_1 = event[6:]

                if event.startswith('Line2 '):
                    self.line_2 = event[6:]

                self.write_lines()

        except Exception as e:
            log.error('Unknown problem with the LCD_16x2_I2C detected', e)

    def clear(self):
        self.screen.lcd_clear()
        log.debug('clear')

    def write_lines(self):

        if self.previous_line_1 != self.line_1:
            self.previous_line_1 = self.line_1
            self.screen.lcd_display_string('                ', 1)
            self.screen.lcd_display_string(self.line_1, 1)

        if self.previous_line_2 != self.line_2:
            self.previous_line_2 = self.line_2
            self.screen.lcd_display_string('                ', 2)
            self.screen.lcd_display_string(self.line_2, 2)

        log.debug('Line 1 value = ' + self.line_1)
        log.debug('Line 2 value = ' + self.line_2)

    def turn_off(self):
        self.screen.backlight(0)
        log.info('turn off backlight')

    def turn_on(self):
        self.screen.backlight(1)
        log.info('turn on backlight')
