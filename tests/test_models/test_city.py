#!/usr/bin/python3
"""unittest for city module"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_default_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == "__main__":
    unittest.main()
