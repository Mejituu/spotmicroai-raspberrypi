#!/usr/bin/env python3

import multiprocessing

import spotmicro.utilities.log as logger
from spotmicro.ultrasonic_sensor_controller.ultrasonic_sensor_controller import UltrasonicSensorController
from spotmicro.motion_controller.motion_controller import MotionController
from spotmicro.lcd_screen_controller.lcd_screen_controller import LCDScreenController
from spotmicro.remote_controller.remote_controller import RemoteControllerController

log = logger.setup_logger()


def process_motion_controller(communication_queues):
    log.info('Firing up Motion controller')
    motion = MotionController(communication_queues)


def process_remote_controller_controller(communication_queues):
    log.info('Firing up Remote Controller controller')
    remote_controller = RemoteControllerController(communication_queues)


# Optional
def process_output_lcd_screen_controller(communication_queues):
    log.info('Firing up LCD Screen controller')
    screen = LCDScreenController(communication_queues)


# Optional, not used, just as an example
def process_ultrasonic_sensor_controller(communication_queues):
    log.info('Firing up Ultrasonic Sensor controller')
    ultrasonic_sensor = UltrasonicSensorController(communication_queues)


def create_controllers_queues():
    log.info('Creating controller queues for communication')
    # https://docs.python.org/3/library/queue.html
    # The reason we use queues for inter process communication is because simplicity
    # Why we use multiple queues? Because we limit the number of messages on them and
    # some sensors read and update them at very high frequency, other don't. Having a sole queue
    # makes the high frequency update controllers to wipe out the slow ones messages.
    # Get and Put methods handle the locks via optional parameter block=True

    communication_queues = {'motion_controller': multiprocessing.Queue(10),
                            'lcd_screen_controller': multiprocessing.Queue(10)}

    return communication_queues


def close_controllers_queues(communication_queues):
    log.info('Closing controller queues')

    for queue in communication_queues.items():
        queue.close()
        queue.join_thread()


def main():
    communication_queues = create_controllers_queues()

    # Start the motion controller
    # 0E port from PCA9685 must be HIGH
    # Process/Thread, listening the events QUEUE for orders
    motion_controller = multiprocessing.Process(target=process_motion_controller, args=(communication_queues,))
    motion_controller.daemon = True  # The daemon process will continue to run as long as the main process is executing
    # and it will terminate after finishing its execution or when the main program would be killed.

    # Activate Bluetooth controller
    # Capture the buttons from the controller and generate events for the QUEUE
    remote_controller_controller = multiprocessing.Process(target=process_remote_controller_controller,
                                                           args=(communication_queues,))
    remote_controller_controller.daemon = True

    # Activate Example sensor controller
    # Adding a sensor example, lets say ultrasonic module
    ultrasonic_sensor_controller = multiprocessing.Process(target=process_ultrasonic_sensor_controller,
                                                           args=(communication_queues,))
    ultrasonic_sensor_controller.daemon = True

    # Activate Screen
    # Show communication on it about the status
    lcd_screen_controller = multiprocessing.Process(target=process_output_lcd_screen_controller,
                                                    args=(communication_queues,))
    lcd_screen_controller.daemon = True

    # Start the threads queue processing
    motion_controller.start()
    remote_controller_controller.start()
    ultrasonic_sensor_controller.start()
    lcd_screen_controller.start()

    # make sure the thread/process ends
    motion_controller.join()
    remote_controller_controller.join()
    ultrasonic_sensor_controller.join()
    lcd_screen_controller.join()

    close_controllers_queues(communication_queues)


if __name__ == '__main__':
    log.info('SpotMicro starting')

    try:
        main()

    except KeyboardInterrupt:
        log.info('Aborted manually with Control+C')

    else:
        log.info('Normal termination')
