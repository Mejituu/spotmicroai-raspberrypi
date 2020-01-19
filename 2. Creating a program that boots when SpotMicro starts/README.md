# SpotMicroPi

Hello, I'm Fran and i'm going to guide you in the steps needed for preparing your RaspberryPi to move your SpotMicro.

From now on, since you are going to use RaspBerryPi to power it, I will call it SpotMicroPi

This part of the tutorial assume you already have the RaspberryPi ready for run a program.

# Hardware requirements for this tutorial

* RaspberryPi 3 or better (4 requires heatsink)
* 16x2 LCD Display Screen with I2C Module Interface Adapter

# Software requirements

* RaspbianLite installed and updated


# Creating our first python program

## Python 3 environment

Open a terminal to the RaspberryPi, remember your password is "spotmicro"

```
ssh pi@192.168.1.XX
```

Make sure youare in the home directory for the user "pi", the following command must return "/home/pi"

```
pwd
```

Lets start working on the program.

The program wil run as a daemon/service in the RaspberryPi, will start every time the SpotMicro get powered.

I'm using Python 3, since is very accesible to everyone and very decent language.

We will create the folder for the program now and start a Python 3 project

```
mkdir spotmicro
cd spotmicro

sudo apt-get install python3-venv -y
```

Create your Python3 environment in the spotmicro folder
```
python3 -m venv venv --clear
```

Activate your Python environment
```
source venv/bin/activate
```
Note the "(env)" in your terminal, that means you have the environment variables needed to run your programs in that folder (were we created the python environment)

![python3-environment-activated](python3-environment-activated.JPG)

Like Raspbian, Python has modules and packages, Raspbian (the OS) uses apt for update and install packages in the system (because is based in Debian), Python uses "pip".

Pip let you install modules in your programs that you can use, for example if you have the I2C 16x2 led screen, you will need its library installed in your Python 3 environment to make it work. Pip does that for you.

Some deprecated versions of Python had issues, to fix them all and avoid entering in problems with them just run the following commands:

```
curl https://bootstrap.pypa.io/get-pip.py | python

pip install --upgrade pip
pip install --upgrade setuptools
```

To deactivate the environment you can always write "deactivate" in your terminal.

And thats about it!, we are ready to create our first hello world python application!

## Python 3 hello world

Lets create fast just a hello_world.py file to print a message and see if all is working as expected.

```
echo "print('SpotMicro Hello World')" > hello_world.py
python3 hello_world.py
```
![hello-world-program](hello-world-program.JPG)


