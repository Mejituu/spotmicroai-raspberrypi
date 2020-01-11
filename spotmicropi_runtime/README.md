This is the SpotMicroPi runtime source code that you can run in the Raspberry Pi inside your SpotMicroPi

SpotMicroPi uses Raspberry Pi, for Jetson Nano there is another repository https://gitlab.com/custom_robots/spotmicro

Depending of your wiring you must configure in the code some I2C addresses and pins. Also if you are using less sensors you can just remove or comments those parts from the code.

This code is meant to be located in /opt/spotmicro_runtime in your SpotMicroPi Raspberry Pi board.

For simplicity I use Raspbian Lite in a SanDisk Extreme 32 GB microSDHC Memory Card. This card has the same specifications than the SanDisk Ultra 32GB Class 10 micro SD for big files copy and read, but the Extreme has far more I/O for small files operations.

The software here must be running right after the Raspberry Pi starts, to do so you need to setup it as deamon in linux.

To connect via SSH to your Raspberry PI you must add to Raspbian Lite your wpa_supplicant.conf file with your wifi network, and using raspi-config enable the ssh service.

The first time you connect to your Raspbian Lite your user is "pi" and your password "raspberry", use raspi-config to change it.

This source code project has been created using the instructions here: https://github.com/franferri/my_katas/tree/master/kata-new-python-project

When you try to clone this project and build, in Windows Mac or Linux in x86 architecture, you may encounter than some python dependencies are not available to be build, like the RPi.GPIO. To solve this issue I have purchased a second Raspberry Pi 4 4GB and use the SD card to be the boot partition and an USB3 external SSD drive for the OS, with an external monitor, keyboard and mouse. Developing in that environment with JetBrains PyCharm is very ok.

