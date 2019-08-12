import unittest
from city_functions import city_country

class NameTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities like 'Manila' work?"""
        whereis = city_country('manila', 'philippines')
        self.assertEqual(whereis, 'The city of Manila is in the country of Philippines.')

unittest.main()