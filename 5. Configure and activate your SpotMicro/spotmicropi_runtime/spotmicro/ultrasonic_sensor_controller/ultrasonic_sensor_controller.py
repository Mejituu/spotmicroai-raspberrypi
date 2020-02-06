import spotmicro.utilities.log as logger
import time
import queue

log = logger.get_default_logger()


class UltrasonicSensorController:

    def __init__(self, communication_queues):
        log.info('STARTING CONTROLLER: Example Ultrasonic Sensor, an example to add more input sensors')

        self._queue = communication_queues['motion_controller']

        log.info('STARTED: Example Ultrasonic Sensor controller')

    def do_someting(self):
        while True:
            self._queue.put('AObstacle at 10cm')
            time.sleep(1)
