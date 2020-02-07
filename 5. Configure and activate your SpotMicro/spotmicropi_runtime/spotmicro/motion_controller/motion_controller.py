import signal
import queue
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
from board import SCL, SDA

from spotmicro.utilities.log import Logger

log = Logger().setup_logger('Motion controller')


class MotionController:

    def __init__(self, communication_queues):
        try:

            log.info('Starting controller...')

            signal.signal(signal.SIGINT, self.exit_gracefully)
            signal.signal(signal.SIGTERM, self.exit_gracefully)

            # Setup I2C PCA9685
            self.i2c = busio.I2C(SCL, SDA)

            self.pca_rear = PCA9685(self.i2c, address=0x40)
            self.pca_rear.frequency = 50

            self.pca_front = PCA9685(self.i2c, address=0x42)
            self.pca_front.frequency = 50

            # Setup servos
            self.servo_rear_shoulder_left = servo.Servo(self.pca_rear.channels[0], min_pulse=352, max_pulse=2664)
            self.servo_rear_leg_left = servo.Servo(self.pca_rear.channels[1], min_pulse=352, max_pulse=2664)
            self.servo_rear_feet_left = servo.Servo(self.pca_rear.channels[3], min_pulse=352, max_pulse=2664)

            self.servo_rear_shoulder_right = servo.Servo(self.pca_rear.channels[15], min_pulse=352, max_pulse=2664)
            self.servo_rear_leg_right = servo.Servo(self.pca_rear.channels[14], min_pulse=352, max_pulse=2664)
            self.servo_rear_feet_right = servo.Servo(self.pca_rear.channels[8], min_pulse=352, max_pulse=2664)

            self.servo_front_shoulder_left = servo.Servo(self.pca_front.channels[11], min_pulse=352, max_pulse=2664)
            self.servo_front_leg_left = servo.Servo(self.pca_front.channels[9], min_pulse=352, max_pulse=2664)
            self.servo_front_feet_left = servo.Servo(self.pca_front.channels[8], min_pulse=352, max_pulse=2664)

            self.servo_front_shoulder_right = servo.Servo(self.pca_front.channels[7], min_pulse=352, max_pulse=2664)
            self.servo_front_leg_right = servo.Servo(self.pca_front.channels[6], min_pulse=352, max_pulse=2664)
            self.servo_front_feet_right = servo.Servo(self.pca_front.channels[4], min_pulse=352, max_pulse=2664)

            self.rest_position()

            self._abort_queue = communication_queues['abort_controller']
            self._motion_queue = communication_queues['motion_controller']
            self._lcd_screen_queue = communication_queues['lcd_screen_controller']

            log.info('Started')

        except Exception as e:
            log.error('No PCA9685 detected', e)

    def exit_gracefully(self, signum, frame):
        log.info('Terminated')
        exit(0)

    def do_process_events_from_queues(self):

        try:

            while True:

                try:

                    # If we don't get an order in 60 seconds we disable the robot.
                    event = self._motion_queue.get()

                    log.debug(event)
                    # if event.startswith('activate'):
                    #    self.activate()

                    # if event.startswith('key press'):
                    #    self.move_to_position_xxx()

                    # if event.startswith('_Obstacle at 10cm'):
                    #    pass

                except queue.Empty as e:
                    # This will happen after 60 seconds of inactivity
                    # If we don't get an order in 60 seconds we disable the robot.
                    log.info('Inactivity lasted 60 seconds, shutting down the servos, '
                                          'press start to reactivate')
                    self._abort_queue.put('abort')

                finally:
                    self.pca_rear.deinit()
                    self.pca_front.deinit()


        except Exception as e:
            log.error('Unknown problem with the PCA9685 detected', e)

    def activate(self):
        self._abort_queue.put('activate_servos')

    def rest_position(self):

        self.servo_rear_shoulder_left.angle = 85
        self.servo_rear_leg_left.angle = 75
        self.servo_rear_feet_left.angle = 30

        self.servo_rear_shoulder_right.angle = 102
        self.servo_rear_leg_right.angle = 120
        self.servo_rear_feet_right.angle = 160

        self.servo_front_shoulder_left.angle = 105
        self.servo_front_leg_left.angle = 65
        self.servo_front_feet_left.angle = 40

        self.servo_front_shoulder_right.angle = 105
        self.servo_front_leg_right.angle = 140
        self.servo_front_feet_right.angle = 165

    def move_to_position_xxx(self):
        pass
