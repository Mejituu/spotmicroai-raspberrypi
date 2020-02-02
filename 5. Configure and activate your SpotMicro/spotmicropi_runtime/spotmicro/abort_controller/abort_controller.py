import signal

import RPi.GPIO as GPIO

import spotmicro.utilities.log as logger

log = logger.get_default_logger()


class AbortController:

    def __init__(self, communication_queues):
        log.info('Loading Abort Controller')

        try:

            signal.signal(signal.SIGINT, self.exit_gracefully)
            signal.signal(signal.SIGTERM, self.exit_gracefully)

            # Abort mechanism
            GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD
            GPIO.setup(17, GPIO.OUT)  # set GPIO24 as an output

            self._queue = communication_queues['abort_controller']
            self.do_process_events_from_queue()

        except Exception as e:
            print("OS error: {0}".format(e) + ': No PCA9685 detected')

    def exit_gracefully(self, signum, frame):
        print('GPIO terminating')
        exit(0)

    def do_process_events_from_queue(self):
        log.info('Abort do_something')

        try:

            while True:
                event = self._queue.get(block=True, timeout=None)
                # event = self._queue.get()

                if event == 'activate_servos':
                    print(event)
                    self.activate_servos()

                if event == 'abort':
                    print(event)
                    self.abort()

        except Exception as e:
            log.error('Unknown problem with the GPIO detected', e)

    def activate_servos(self):

        GPIO.output(17, 1)  # set port/pin value to 1/GPIO.HIGH/True

    def abort(self):

        GPIO.output(17, 0)  # set port/pin value to 0/GPIO.LOW/False
