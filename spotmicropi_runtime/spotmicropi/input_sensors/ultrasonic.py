import spotmicropi.utilities.log as logger
import time

log = logger.get_default_logger()


class UltrasonicSensor:

    def __init__(self, events_queue):
        log.info('Loading Ultrasonic Sensor')
        self._events_queue = events_queue

        self.do_someting()

    def do_someting(self):
        log.info('UltrasonicSensor do_something')

        while True:
            self._events_queue.put('Obstacle at 10cm')
            time.sleep(1)
