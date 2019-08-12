import unittest
from city_functions import city_country

class NameTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities like 'Manila' work?"""
        where_is = city_country('manila', 'philippines')
        self.assertEqual(where_is, 'The city of Manila is in the country of Philippines.')

    def test_city_country_population(self):
        """Do cities like 'Manila' with a known population work?"""
        where_is = city_country('manila', 'philippines', '12,877,253')
        self.assertEqual(where_is, 'The city of Manila is in the country of Philippines.'
                                   '\nThe population of Manila, Philippines is 12,877,253.')

unittest.main()