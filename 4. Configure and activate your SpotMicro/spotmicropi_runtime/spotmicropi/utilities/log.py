import logging

SPOTMICROPI = 'SpotMicroPi'


def get_default_logger():
    return get_logger(SPOTMICROPI)


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    return logger


def setup_logger(logger_name=SPOTMICROPI):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    logging_file_handler = logging.FileHandler('logs/' + logger_name + '.log')
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

    return logger
