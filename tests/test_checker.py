import unittest
from unittest.mock import *

from src.sample.checker import *


class TestChecker(unittest.TestCase):
    def test_checker_after_17(self):
        musicName = 'example.mp3'
        checker = Checker()
        checker.env.getTime = Mock(name='getTime')
        checker.env.getTime.return_value = 21
        checker.env.wavWasPlayed = Mock(name="wavWasPlayed")
        checker.env.wavWasPlayed.return_value = True

        result = checker.env.wavWasPlayed(musicName)
        checker.env.resetWav(musicName)

        self.assertEqual(result, True)

    def test_checker_before_17(self):
        musicName = 'example.mp3'
        checker = Checker()
        checker.env.getTime = Mock(name='getTime')
        checker.env.getTime.return_value = 13
        checker.env.wavWasPlayed = Mock(name="wavWasPlayed")
        checker.env.wavWasPlayed.return_value = False

        result = checker.env.wavWasPlayed(musicName)
        checker.env.resetWav(musicName)

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
