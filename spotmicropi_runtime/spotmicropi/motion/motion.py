import spotmicropi.utilities.log as logger
import time

log = logger.get_default_logger()


class Motion:

    def __init__(self, events_queue):
        log.info('Loading Motion')
        self._events_queue = events_queue

        self.do_someting()

    def do_someting(self):
        log.info('Motion do_something')

        while True:
            event = self._events_queue.get()

            if event.startswith('key press'):
                print(event)

            if event.startswith('Obstacle at 10cm'):
                print(event)

            time.sleep(1/3)
