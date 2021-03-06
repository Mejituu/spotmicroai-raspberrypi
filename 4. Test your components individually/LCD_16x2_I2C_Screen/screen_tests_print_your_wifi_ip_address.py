#!/home/pi/spotmicro/venv/bin/python3 -u

import RPi_LCD_16x2_I2C_driver
import socket
import fcntl
import struct

mylcd = RPi_LCD_16x2_I2C_driver.lcd()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s'.encode('utf-8'), ifname[:15].encode('utf-8'))
    )[20:24])

mylcd.lcd_display_string("IP Address:", 1) 

mylcd.lcd_display_string(get_ip_address('wlan0'), 2)
