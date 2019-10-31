import unittest

from city_functions import get_city_country

class CitiesTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py"""
	
	def test_city_country(self):
		"""Do cities like 'Santiago, Chile' work?"""
		city_country = get_city_country('santiago', 'chile')
		self.assertEqual(city_country, 'Santiago, Chile')
	
	def test_city_country_population(self):
		"""Do cities like 'Santiago, Chile' with populations work?"""
		city_country = get_city_country('santiago', 'chile', 50000000)
		self.assertEqual(city_country, 'Santiago, Chile - Population: 50000000')
	

unittest.main()
