import spotmicro.utilities.log as logger
import time

log = logger.get_default_logger()


class UltrasonicSensorController:

    def __init__(self, communication_queues):
        log.info('Loading Ultrasonic Sensor Controller')
        self._queue = communication_queues['motion_controller']

        self.do_someting()

    def do_someting(self):
        log.info('UltrasonicSensor do_something')

        while True:
            self._queue.put('Obstacle at 10cm')
            time.sleep(1)
