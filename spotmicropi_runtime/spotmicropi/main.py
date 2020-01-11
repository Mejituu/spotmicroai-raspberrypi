import spotmicropi.utilities.log as logger

log = logger.get_logger('SpotMicroPi')


class SpotMicroPi:

    def __init__(self):
        log.info('Loading SpotMicroPi')
        pass

    def setup(self):
        log.info('Setup')
        pass

    def init(self):
        log.info('Init')
        pass


if __name__ == '__main__':
    spotmicropi = SpotMicroPi()

    spotmicropi.setup()
    spotmicropi.init()
