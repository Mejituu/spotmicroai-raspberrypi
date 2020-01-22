# SpotMicroAI

Hello, I'm Fran and i'm going to guide you in the steps needed for preparing your RaspberryPi to move your SpotMicro.

We are going to test 3 hardware parts using our program, to familiaryze ourselves with them:

* Screen
* Servos
* Bluetooth controller
  * XBox controller test
  * PS4 controller test

# Hardware requirements

* RaspberryPi 3 or newer recommended
* RaspberryPi power supply
* SD Card with Raspbian Lite
* Wifi connection (or Ethernet)
* A computer like the one you are probably using to read this document

* The Servos connected to a PCA96xx board, and the PCA96xx board connected to the RaspberryPi using I2C
* The Screen connected to the RaspberryPi using I2C
* XBox/PS4 controller connected to the RaspberryPi using Bluetooth

Nothing else, nothing more. All set then, lets go!

# Prepare the system

## Enable I2C

Remember you can use FileZilla or terminal to navigate and update the files in SpotMicroAI.

To run the tests you need to use the terminal.


Open a terminal and run the following commands
```
ssh pi@192.168.1.XX
sudo raspi-config
```

And from the options presented, do the following changes:

* Interfacing options
  * Enable I2C

![raspi-config-enable-i2c.JPG](raspi-config-enable-i2c.JPG)

* Select Finish and accept the reboot option

## Creating the QA tests

Once the reboot finishes, login again, open a terminal and run the following commands
```
ssh pi@192.168.1.XX
cd spotmicro
source venv/bin/activate

mkdir qa_test
cd qa_test/

mkdir screen
mkdir servos
mkdir xboxcontroller
mkdir ps4controller
```

# Testing the Screen

TODO:
* Following: http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/
* https://gitlab.com/custom_robots/spotmicro/raspberrypi/tree/master/4.%20Test%20your%20components%20individually/raw_tests/screen_tests

# Testing the Servos

TODO:
* Following: https://github.com/adafruit/Adafruit_Python_PCA9685
* PDF: https://cdn-learn.adafruit.com/downloads/pdf/adafruit-16-channel-servo-driver-with-raspberry-pi.pdf
* https://gitlab.com/custom_robots/spotmicro/raspberrypi/tree/master/4.%20Test%20your%20components%20individually/raw_tests/servos_tests

# Testing the XBox controller

TODO:
* https://pimylifeup.com/xbox-controllers-raspberry-pi/
* https://gist.github.com/rdb/8864666
* https://gitlab.com/custom_robots/spotmicro/raspberrypi/tree/master/4.%20Test%20your%20components%20individually/raw_tests/xboxcontroller

# Testing the PS4 controller

TODO:
* DS4 driver