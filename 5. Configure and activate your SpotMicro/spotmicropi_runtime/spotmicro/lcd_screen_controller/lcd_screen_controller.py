import signal
import sys
import time
from spotmicro.utilities.log import Logger
from spotmicro.lcd_screen_controller import LCD_16x2_I2C_driver
from spotmicro.utilities.config import Config

log = Logger().setup_logger('LCD Screen controller')


class LCDScreenController:
    is_alive = False

    def __init__(self, communication_queues):
        try:

            log.debug('Starting controller...')

            signal.signal(signal.SIGINT, self.exit_gracefully)
            signal.signal(signal.SIGTERM, self.exit_gracefully)

            i2c_address = int(Config().get('lcd_screen_controller[0].lcd_screen[0].address'), 0)

            self.screen = LCD_16x2_I2C_driver.lcd(address=i2c_address)

            self._lcd_screen_queue = communication_queues['lcd_screen_controller']

            self.line_1 = 'SpotMicro'
            self.line_2 = ''

            self.previous_line_1 = ''
            self.previous_line_2 = ''

            self.clear()
            self.turn_on()
            self.write_lines()

            self.is_alive = True
            log.info('Controller started')

        except Exception as e:
            self.is_alive = False
            log.error('LCD Screen problem detected, skipping module')

    def exit_gracefully(self, signum, frame):
        self.clear()
        self.turn_off()
        log.info('Terminated')
        sys.exit(0)

    def do_process_events_from_queue(self):

        if not self.is_alive:
            log.error("SpotMicro can work without lcd_screen, continuing")
            return

        try:
            while True:
                event = self._lcd_screen_queue.get()

                if event.startswith('Line1 '):
                    self.line_1 = event[6:]

                if event.startswith('Line2 '):
                    self.line_2 = event[6:]

                self.write_lines()

                time.sleep(2)

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

    def status_icons(self):

        self.screen.lcd_clear()

        # let's define a custom icon, consisting of 6 individual characters
        # 3 chars in the first row and 3 chars in the second row
        fontdata1 = [
            # Char 0 - Upper-left
            [0x00, 0x00, 0x03, 0x04, 0x08, 0x19, 0x11, 0x10],
            # Char 1 - Upper-middle
            [0x00, 0x1F, 0x00, 0x00, 0x00, 0x11, 0x11, 0x00],
            # Char 2 - Upper-right
            [0x00, 0x00, 0x18, 0x04, 0x02, 0x13, 0x11, 0x01],
            # Char 3 - Lower-left
            [0x12, 0x13, 0x1b, 0x09, 0x04, 0x03, 0x00, 0x00],
            # Char 4 - Lower-middle
            [0x00, 0x11, 0x1f, 0x1f, 0x0e, 0x00, 0x1F, 0x00],
            # Char 5 - Lower-right
            [0x09, 0x19, 0x1b, 0x12, 0x04, 0x18, 0x00, 0x00],
            # Char 6 - my test
            [0x1f, 0x0, 0x4, 0xe, 0x0, 0x1f, 0x1f, 0x1f],
        ]

        # Load logo chars (fontdata1)
        self.screen.lcd_load_custom_chars(fontdata1)

        # Write first three chars to row 1 directly
        self.screen.lcd_write(0x80)
        self.screen.lcd_write_char(0)
        self.screen.lcd_write_char(1)
        self.screen.lcd_write_char(2)
        # Write next three chars to row 2 directly
        self.screen.lcd_write(0xC0)
        self.screen.lcd_write_char(3)
        self.screen.lcd_write_char(4)
        self.screen.lcd_write_char(5)
