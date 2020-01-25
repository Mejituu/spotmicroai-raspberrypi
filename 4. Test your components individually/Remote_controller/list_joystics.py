#!/home/pi/spotmicro/venv/bin/python3 -u

from __future__ import print_function
from inputs import devices

def main():

    print("We have detected the following devices:\n")

    for device in devices:
        print(device)


if __name__ == "__main__":
    main()
