import unittest
from city_functions import get_formatted_city_country_name

class NamesTasteCase(unittest.TestCase):
    """Test for 'city_functions.py'."""

    def test_city_country(self):
        """Do names like 'Seoul, South Korea' work?"""
        formatted_name = get_formatted_city_country_name('seoul', 'south korea')
        self.assertEqual(formatted_name, 'Seoul, South Korea')

    def test_city_country_population(self):
        """Do names like 'Santiago', 'Chile - population 5_000_000' work?"""
        formatted_name = get_formatted_city_country_name('santiago', 'chile',
            '5_000_000')
        self.assertEqual(formatted_name,
            'Santiago, Chile - Population 5_000_000')
if __name__ == '__main__':
    unittest.main()
