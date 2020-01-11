import logging


def setup_logging():
    logger = logging.getLogger('spotmicropi')
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    logging_file_handler = logging.FileHandler('spotmicropi.log')
    logging_file_handler.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    logging_stream_handler = logging.StreamHandler()
    logging_stream_handler.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging_file_handler.setFormatter(formatter)
    logging_stream_handler.setFormatter(formatter)

    # add the handlers to logger
    logger.addHandler(logging_file_handler)
    logger.addHandler(logging_stream_handler)


class SpotMicroPi:
    logger = logging.getLogger('spotmicropi')

    def setup(self):
        self.logger.info('Loading SpotMicroPi')

    def init(self):
        pass


if __name__ == '__main__':
    setup_logging()
    spotmicropi = SpotMicroPi()

    spotmicropi.setup()
    spotmicropi.init()
