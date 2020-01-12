#!/usr/bin/env python3

import spotmicropi.utilities.log as logger
import multiprocessing

from spotmicropi.motion.motion import Motion
from spotmicropi.remote_controllers.remote_controller import RemoteController
from spotmicropi.input_sensors.ultrasonic import UltrasonicSensor

log = logger.setup_logger()


def process_motion_controller(events_queue):
    log.info('Motion Controller')
    motion = Motion(events_queue)


def process_remote_controller(events_queue):
    log.info('Remote Controller')
    remote_controller = RemoteController(events_queue)


def process_ultrasonic_sensor(events_queue):
    log.info('Ultrasonic Sensor')
    ultrasonic_sensor = UltrasonicSensor(events_queue)


if __name__ == '__main__':
    log.info('SpotMicroPi')

    _events_queue = multiprocessing.Queue(10)

    # Start the motion controller
    # 0E port from PCA9685 must be HIGH
    # Process/Thread, listening the events QUEUE for orders

    motion_controller = multiprocessing.Process(target=process_motion_controller, args=(_events_queue,))
    motion_controller.daemon = True

    # Activate Bluetooth controller
    # Capture the buttons from the controller and generate events for the QUEUE

    remote_controller = multiprocessing.Process(target=process_remote_controller, args=(_events_queue,))
    remote_controller.daemon = True

    # Activate Example sensor controller
    # Adding a sensor example, lets say ultrasonic module

    ultrasonic_sensor = multiprocessing.Process(target=process_ultrasonic_sensor, args=(_events_queue,))
    ultrasonic_sensor.daemon = True

    # Activate Screen
    # Show communication on it about the status

    # Start the threads queue processing
    motion_controller.start()
    remote_controller.start()
    ultrasonic_sensor.start()

    motion_controller.join()  # make sure the thread ends
    remote_controller.join()  # make sure the thread ends
    ultrasonic_sensor.join()

    _events_queue.close()
    _events_queue.join_thread()
