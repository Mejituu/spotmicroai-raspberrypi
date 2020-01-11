import unittest

from spotmicropi.main import SpotMicroPi


class SpotMicroPiTestCase(unittest.TestCase):

    def test_barks_in_spanish(self):
        # given
        spotmicropi = SpotMicroPi()

        # when

        # then
        self.assertEqual(spotmicropi._spanish_bark, spotmicropi.bark_in_spanish())

    def test_barks_in_japanese(self):
        # given
        spotmicropi = SpotMicroPi()

        # when

        # then
        self.assertEqual(spotmicropi._japanese_bark, spotmicropi.bark_in_japanese())

    def test_barks_in_german(self):
        # given
        spotmicropi = SpotMicroPi()

        # when

        # then
        self.assertEqual(spotmicropi._german_bark, spotmicropi.bark_in_german())

    def test_barks_in_english(self):
        # given
        spotmicropi = SpotMicroPi()

        # when

        # then
        self.assertEqual(spotmicropi._english_bark, spotmicropi.bark_in_english())


if __name__ == '__main__':
    unittest.main()
