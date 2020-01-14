import I2C_LCD_driver
from time import *
import argparse
import socket
import fcntl
import struct

parser = argparse.ArgumentParser()
parser.add_argument("temp")
args = parser.parse_args()

mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s'.encode('utf-8'), ifname[:15].encode('utf-8'))
    )[20:24])


mylcd.lcd_display_string(args.temp, 1)
mylcd.lcd_display_string(get_ip_address('wlan0'), 2)
