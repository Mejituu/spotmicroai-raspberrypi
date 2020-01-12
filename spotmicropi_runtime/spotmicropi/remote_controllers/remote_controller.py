import spotmicropi.utilities.log as logger
import time

log = logger.get_default_logger()


class RemoteController:

    def __init__(self, events_queue):
        log.info('Loading Remote Controller')
        self._events_queue = events_queue

        self.do_someting()

    def do_someting(self):
        log.info('RemoteController do_something')

        while True:
            self._events_queue.put('key press A')
            time.sleep(1)
