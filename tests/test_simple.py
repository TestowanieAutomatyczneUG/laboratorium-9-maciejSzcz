# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
from unittest.mock import *

from src.sample.simple import *


class TestSimple(unittest.TestCase):

    def test_needsFuel(self):
        test_car = Car()
        test_car.needsFuel = Mock(name = 'needsFuel')
        test_car.needsFuel.return_value = False

        self.assertEqual(test_car.needsFuel(), False)

    
    def test_getEngineTemperature(self):
        test_car = Car()
        test_car.getEngineTemperature = Mock(name = 'getEngineTemperature')
        test_car.getEngineTemperature.return_value = 91

        self.assertEqual(test_car.getEngineTemperature(), 91)

    def test_driveTo(self):
        destination = 'San Francisco'
        test_car = Car()
        test_car.driveTo = Mock(name = 'driveTo')
        test_car.driveTo.return_value = f'Drive to {destination}'

        self.assertEqual(test_car.driveTo('Miami'), 'Drive to San Francisco')

if __name__ == '__main__':
    unittest.main()
