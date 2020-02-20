# SpotMicroAI

Hello, I'm Fran and i'm going to guide you in the steps needed for preparing your RaspberryPi to move your SpotMicro.

In order to have SpotMicroAI moving we need to prepare its operating system in a SD card.

RaspberryPi fundation has written a very nice manual here: https://www.raspberrypi.org/documentation/installation/installing-images/ guiding you step by step.

But in this manual I'm going to do it a bit differently, I will drive you for an installation that don't need any screen, monitor and keyboard connected to your RaspberryPi to acomplish it. You just need a WIFI connection and or network cable connection.

This kind of installation is called headless.

The concept is very simple, in a nutshell, before we boot the RaspberryPi with our SD, the SD will have the network configuration (WIFI or nothing if you prefer to use network cable). Also will have the configuration needed to enable the services to access to it (VNC and SSH).

# Hardware requirements

This manual covers the installation of the operating system in the RaspberryPi, and letting it accesible wirelessly

* RaspberryPi 3 or newer recommended
* RaspberryPi power supply
* SD Card
* Wifi connection (or Ethernet)
* A computer like the one you are probably using to read this document

Nothing else, nothing more. All set then, lets go!

# RaspberryPi operating system

Raspbian is the official operating system for RaspberryPi. To simplify its installation and provide the user more options RaspberryPi fundation created NOOBS, which let you install other operating systems in the platform.

NOOBS is a small operating system that runs before your operating system (In this case before Raspbian) to let you install it in a very simple and convinient maner. But NOOBS has a problem, when you enable VNC for it, disables the external monitor.

We are going to use PINN, the reason is that brings more options to the table, like a convinient VNC implementation and advanced options if needed. PINN is a version of the NOOBS Operating System Installer for Raspberry Pi.

To summarize, we are going to use PINN to install RaspbianLite in our SD card without keyboard/mouse/screen attached to it.

You can read all about it here: https://github.com/procount/pinn

## Step 1

PINN is just a compressed zip file that we must extract its contents in the SD card.

Download the .zip file that contains PINN from: http://sourceforge.net/projects/pinn/files/pinn-lite.zip

![pinn-lite-zip-download](pinn-lite-zip-download.JPG)


## Step 2

We need to format the SD card. Do this step even if the SD card is new.

In the RaspberryPi website, during the official installation guide, they recommend the following tool: https://www.sdcard.org/downloads/formatter/, and is the one you must use.

* Dowload the executable for your operating system.
* Install the "SD Card Formatter" tool that you just download
* Insert in the computer the SD card
* Run the "SD Card Formatter"
* Make sure you select the proper card (the tool is smart to show you only SD cards)
* Format the card (all defaults)

![sd-card-formatter](sd-card-formatter.JPG)


![sd-card-formatted](sd-card-formatted.JPG)


## Step 3

We need to put all PINN files in the SD card, is that simple!

* Unzip the **pinn-lite.zip** file you downloaded previously in the SD card

The SD card must look like similar to the following image:

![unzip-pinns-in-sd-card](unzip-pinns-in-sd-card.JPG)


## Step 4

Is time to configure the PINN operating system to boot with VNC and SSH enabled, so we can access it using our network.

Doing this, we dont need mouse/keyboard/screen connected to our RaspberryPi, not even during the installation. But we can have them of course.

* Open the SD card
* Make sure in your OS you can see the file extensions
* Open the file **recovery.cmdline** with a proper text editor like Sublime Text or nano
* Add the following 2 words to the line present in the file:
  * vncshare
  * ssh

It will result in something like:

```
runinstaller quiet ramdisk_size=32768 root=/dev/ram0 init=/init vt.cur_default=1 elevator=deadline repo_list=http://raw.githubusercontent.com/procount/pinn-os/master/os/repo_list.json loglevel=2 sdhci.debug_quirks2=4 vncshare ssh
```

* Save the file

## Step 5

Enable ssh by default when RaspbianLite starts for the first time

* Create an empty text file in the sd card root, called **ssh**

## Step 6

Lets connect to the network!

If you don't have a WIFI network just plug the cable in the RaspberryPi and skip this step, but mind SpotMicroAI will need this cable to be "programmed" every time.

In order to enable the WIFI:

* Open the SD card
* Create a text file called **wpa_supplicant.conf**
* Write in the file the following lines

```
country=us
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 scan_ssid=1
 ssid="YOUR_WIFI_SSID_NAME_HERE"
 psk="SUPER_SECRET_PASSWORD"
}
```

* Save the file

## Step 7 - (Optional step) - Offline installation

If your WIFI network don't have access to internet, you can also load the Raspbian Lite image in the SD card.

* In your SD card, go to the "os" folder create a folder called "raspbian_lite"
* From the official online repository (http://downloads.raspberrypi.org/raspbian_lite/), download all files to your "raspbian_lite" folder on the SD card (skip the folder archive and images).
* There is a file called marketing.tar, uncompress it in the raspbian_lite folder of your SDcard, it will create a folder called slides_vga with a few images in

This makes PINN not having to download it when selected.

## Step 8

Lets boot the RaspberryPi

* Insert the SD card in the RaspberryPi
* Connect the power supply to the RaspberryPi
* Boot it

# Network access

Connecto to your Router and identify which IP has been assigned to your RaspberryPi.

For convenience you must add a IP Address reservation in your DCHP Server, so your RasberryPi IP will be always the same.

Every router is different, I'm affraid I cant help you more here.

The IP will look like something like 192.168.1.XX for an standard home router installation.

![router-dhcp-server-configuration](router-dhcp-server-configuration.JPG)

Once you know the IP ping to it to be sure you can reach it.

* Connect to your router (most likely 192.168.1.1)
* Identify the RaspberryPi in your list of WIFI clients
* From a console try to ping the ip
    
```
ping 192.168.1.XX
```

![ping-raspberrypi-ip-address](ping-raspberrypi-ip-address.JPG)

* In your router homepage make the IP reservation to have it permanently assigned
* Save configuration

# Connect to the RaspberryPI via VNC

In order to see the PINN "virtual screen" that VNC provides, you need to install the VNC Viewer. VNC Viewer is a free to use software.

![router-dhcp-server-configuration](vnc-viewer-download.JPG)

* Download VNC Viewer from https://www.realvnc.com/en/connect/download/viewer/
* Install VNC Viewer
* Connect to the RaspberryPi

![vnc-viewer](vnc-viewer.JPG)

* A wild unencrypted notice will appear!

![vnc-viewer-connect-certifi](vnc-viewer-connect-certificate.JPG)

* Mark "Don't warm me about this again on this computer"
* Press continue

![pinn](pinn.JPG)


# PINN installing Headless RasbianLite

* At the bottom of the screen select the language "English (US)" and the keyboard of your preference, for example Keyboard "us"

* In the main window Navigate to the **Minimal tab**
* Select Raspbian Lite from the list
* Press Install

![pinn-raspbian-lite-installation](pinn-raspbian-lite-installation.JPG)

Since we have PINN with ssh also configured, it will enable ssh on the first boot of RaspbianLite and we will be able to access it from the terminal console.

From now on there is no more graphical environment. After all, this RaspberryPi is going to be in the body of the SpotMicroAI reacting to events, so, will perform better without graphical environment.

![pinn-raspbian-lite-installation-done](pinn-raspbian-lite-installation-done.JPG)

After clicking OK when the installation is done, you will lose VNC connectivity.

* Close VNC


# RasbianLite

## Step 1

* Open a terminal (Windows command prompt/PowerShell or Mac/Linux terminal) and execute the following command to access your RaspberryPi by ssh:

```
ssh pi@192.168.1.XX

```

Now you wil be ask to add the ssh key to your key store, just say yes.

![raspbian-first-ssh](raspbian-first-ssh.JPG)

Now it will prompt you about the password, type "raspberry"

![raspbian-first-ssh-password](raspbian-first-ssh-password.JPG)

You are logged in!

![raspbian-first-ssh-login](raspbian-first-ssh-login.JPG)

## Step 2

Lets update the system, run the following commands:

```
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get autoremove -y
```

While the update is happening, open a second terminal and monitor the temperature

```
ssh pi@192.168.1.XX
/opt/vc/bin/vcgencmd measure_temp
```
It will show you something like "temp=55.0'C"

If you get beyond 60ºC you need a heatsink covering the chips of the board. RaspberryPi 4 needs it.

## Step 3

Is time to configure the SpotMicroAI system.

Write the following command in any of the open windows:

```
sudo raspi-config
```

And from the options presented, do the following changes:

* Change user password to "spotmicro"

* Network options -> Hostname -> Change hostname to "spotmicro"

* Localization options
  * Change Locale, remove "en_GB.xxx" and select "en_US.UTF-8 UTF-8"
    * It will prompt about "Default locale for the system environment", select "en_US.UTF-8"
  * Select your timezone, acording your real location
  * Change Wifi country, acording your real location

* Select Finish and accept the reboot option

Your terminal windows will lose connectivity.

Reconnect to the SpotMicroAI, remember your password is now "spotmicro"

```
ssh pi@192.168.1.XX
sudo raspi-config
```

And from the options presented, select:

* Update


# SpotMicroAI

**You are all set!**

Now your SpotMicroAI has a soul.
You need a program now to wake it up when it boots, we need a program that will start when we power it up.
