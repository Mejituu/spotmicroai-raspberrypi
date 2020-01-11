class SpotMicroPi:

    def setup(self):
        return "setup"

    def init(self):
        return "init"


if __name__ == '__main__':
    spotmicropi = SpotMicroPi()

    spotmicropi.setup()
    spotmicropi.init()
