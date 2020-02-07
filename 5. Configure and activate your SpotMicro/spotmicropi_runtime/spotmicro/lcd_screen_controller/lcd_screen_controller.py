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

            self.screen.lcd_clear()
            self.screen.backlight(1)
            self.screen.lcd_display_string('SpotMicro', 1)

            log.info('Started')

        except Exception as e:
            log.error('LCD Screen problem detected', e)

    def exit_gracefully(self, signum, frame):
        self.screen.lcd_clear()
        self.screen.backlight(0)
        log.info('Terminated')
        exit(0)

    def do_process_events_from_queue(self):

        try:
            while True:
                event = self._lcd_screen_queue.get()

                if event.startswith('Line1 '):
                    self.write_first_line(event[6:])

                if event.startswith('Line2 '):
                    self.write_second_line(event[6:])

                time.sleep(1 / 3)

        except Exception as e:
            log.error('Unknown problem with the LCD_16x2_I2C detected', e)

    def clear(self):
        self.screen.lcd_clear()
        log.info('clear')

    def write_first_line(self, line_text):
        self.screen.lcd_display_string(line_text, 1)
        log.info('Line 1 value = ' + line_text)

    def write_second_line(self, line_text):
        self.screen.lcd_display_string(line_text, 2)
        log.info('Line 2 value = ' + line_text)

    def turn_off(self):
        log.info('turn_off')

    def turn_on(self):
        log.info('turn_on')
