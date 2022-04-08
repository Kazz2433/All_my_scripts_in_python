import unittest
from city_functions import city_counrty

class CityTestCase(unittest.TestCase):
    
    def test_city_country(self):
        fullname = city_counrty("london","england",'10000')
        self.assertEqual(fullname, "London, England - 10000" )

unittest.main()