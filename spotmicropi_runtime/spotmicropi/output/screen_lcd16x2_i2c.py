import spotmicropi.utilities.log as logger
import time

log = logger.get_default_logger()


class ScreenLCD16x2I2c:

    def __init__(self, events_queue):
        log.info('Loading ScreenLCD16x2I2c')
        self._events_queue = events_queue

        self.do_someting()

    def do_someting(self):
        log.info('ScreenLCD16x2I2c do_something')

        while True:
            event = self._events_queue.get()

            if event.startswith('screen'):
                print(event)

            time.sleep(1 / 3)

    def setup(self, ):
        log.info('Loading ScreenLCD16x2I2c')
        # _i2c_address = read config from file
        # print(int(i2c_address))

    def clear(self):
        pass

    def write_first_line(self):
        pass

    def write_second_line(self):
        pass

    def turn_off(self):
        pass

    def turn_on(self):
        pass
