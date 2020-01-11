import spotmicropi.utilities.log as logger

log = logger.get_default_logger()


class ScreenLCD16x2I2c:

    def __init__(self, i2c_address=40):
        log.info('Loading ScreenLCD16x2I2c')
        _i2c_address = i2c_address
        print(int(i2c_address))

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
