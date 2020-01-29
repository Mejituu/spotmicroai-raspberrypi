
# Pull the runtime in your development environment

```
cd ~

mkdir projects
cd projects

git clone https://gitlab.com/custom_robots/spotmicro/raspberrypi.git

cd "raspberrypi/5. Configure and activate your SpotMicro/spotmicropi_runtime"

python3 -m venv venv --clear

source venv/bin/activate

curl https://bootstrap.pypa.io/get-pip.py | python

pip install --upgrade pip
pip install --upgrade setuptools

```

```
rsync -avz --delete --exclude-from .gitignore "franferri@192.168.1.107:/Users/franferri/projects/raspberrypi/5.\ Configure\ and\ activate\ your\ SpotMicro/*" /home/pi/projects/raspberrypi/5.\ Configure\ and\ activate\ your\ SpotMicro/
```


# Booting SpotMicroAI with all data

systemd with venv: https://stackoverflow.com/questions/37211115/how-to-enable-a-virtualenv-in-a-systemd-service-unit
Remember to use: sudo systemctl daemon-reload
when we change a service

do something on shudown signal: https://stackoverflow.com/questions/39275948/python-detect-linux-shutdown-and-run-a-command-before-shutting-down

https://medium.com/@kevalpatel2106/monitor-the-core-temperature-of-your-raspberry-pi-3ddfdf82989f






chmod +x spotmicro.py

```
#!/home/pi/spotmicro/venv/bin/python3 -u

import LCD_I2C_driver
import socket
import fcntl
import struct
import os
import time
import signal

mylcd = LCD_I2C_driver.lcd()

def stop(sig, frame):
    global stopped
    stopped = True
    mylcd.lcd_clear()
    mylcd.lcd_display_string("GoodBye", 1)
    mylcd.lcd_display_string("", 2)
    time.sleep(3)

signal.signal(signal.SIGTERM, stop)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s'.encode('utf-8'), ifname[:15].encode('utf-8'))
    )[20:24])

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

mylcd = LCD_I2C_driver.lcd()

while True:
    print('SpotMicro updating LCD')
    mylcd.lcd_clear()
    mylcd.lcd_display_string('Temp: ' + measure_temp().rstrip(),1)
    mylcd.lcd_display_string(get_ip_address('wlan0'), 2)
    time.sleep(5)
```



# Servos speed and specs

    Giro 180º

    Velocidad para
        4.8v       0.17s for 60º
        6v         0.14s for 60º

    ChangeDutyCycle 2.5, 7.5 a 12.5

    if the travel needs more than 60º, we need to send more than 1 pulse
    p.ChangeDutyCycle(2.5)






