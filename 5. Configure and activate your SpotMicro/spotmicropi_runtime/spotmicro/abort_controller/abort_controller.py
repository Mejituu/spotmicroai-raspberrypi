import signal
import queue
import RPi.GPIO as GPIO

from spotmicro.utilities.log import Logger

log = Logger().setup_logger('Abort controller')


class AbortController:

    def __init__(self, communication_queues):

        try:

            log.info('Starting controller...')

            signal.signal(signal.SIGINT, self.exit_gracefully)
            signal.signal(signal.SIGTERM, self.exit_gracefully)

            # Abort mechanism
            GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD
            GPIO.setup(17, GPIO.OUT)  # set GPIO24 as an output

            self._abort_queue = communication_queues['abort_controller']
            self._lcd_screen_queue = communication_queues['lcd_screen_controller']

            log.info('Started')

        except Exception as e:
            log.error('GPIO problem detected', e)

    def exit_gracefully(self, signum, frame):
        log.info('Terminated')
        exit(0)

    def do_process_events_from_queue(self):

        try:

            while True:
                event = self._abort_queue.get()
                # event = self._queue.get()

                if event == 'activate_servos':
                    self.activate_servos()

                if event == 'abort':
                    self.abort()

        except Exception as e:
            log.error('Unknown problem with the GPIO detected', e)

    def activate_servos(self):

        GPIO.output(17, 1)  # Set GPIO pin value to 1/GPIO.HIGH/True

    def abort(self):

        GPIO.output(17, 0)  # set GPIO pin value to 0/GPIO.LOW/False
