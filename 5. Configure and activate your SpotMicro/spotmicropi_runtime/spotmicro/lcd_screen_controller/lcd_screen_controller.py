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

        self.status_icons()

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

        custom_icons = []

        icon_empty = [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
        icon_success = [0x0, 0x1, 0x3, 0x16, 0x1c, 0x8, 0x0, 0x0]
        icon_pca9685 = [0x1f, 0x11, 0x15, 0x15, 0x15, 0x15, 0x11, 0x1f]
        icon_gpio = [0x4, 0x4, 0x1f, 0x0, 0x0, 0xe, 0x4, 0x4]
        icon_remote_controller = [0x11, 0xa, 0xe, 0xa, 0xa, 0xe, 0xa, 0x11]
        icon_temperature = [0x18, 0x18, 0x3, 0x4, 0x4, 0x4, 0x3, 0x0]
        icon_problem = [0x0, 0x1b, 0xe, 0x4, 0xe, 0x1b, 0x0, 0x0]

        custom_icons.insert(0, icon_empty)
        custom_icons.insert(1, icon_success)
        custom_icons.insert(2, icon_pca9685)
        custom_icons.insert(3, icon_gpio)
        custom_icons.insert(4, icon_remote_controller)
        custom_icons.insert(5, icon_temperature)
        custom_icons.insert(6, icon_problem)
        #  custom_icons.insert(7,XXX)

        self.screen.lcd_load_custom_chars(custom_icons)

        # Write first three chars to row 1 directly
        self.screen.lcd_write(0x80)

        for char in 'SpotMicro':
            self.screen.lcd_write(ord(char), 0b00000001)

        self.screen.lcd_write_char(0)
        self.screen.lcd_write_char(4)
        self.screen.lcd_write_char(0)
        self.screen.lcd_write_char(3)
        self.screen.lcd_write_char(0)
        self.screen.lcd_write_char(2)
        self.screen.lcd_write_char(2)

        # Write next three chars to row 2 directly
        self.screen.lcd_write(0xC0)
        self.screen.lcd_write_char(0)
        self.screen.lcd_write_char(0)
        self.screen.lcd_write_char(0)
        self.screen.lcd_write_char(0)
        self.screen.lcd_write_char(0)
        self.screen.lcd_write_char(0)
        for char in '45':
            self.screen.lcd_write(ord(char), 0b00000001)

        self.screen.lcd_write_char(5)
        self.screen.lcd_write_char(0)
        self.screen.lcd_write_char(6)
        self.screen.lcd_write_char(0)
        self.screen.lcd_write_char(1)
        self.screen.lcd_write_char(0)
        self.screen.lcd_write_char(1)
        self.screen.lcd_write_char(1)
