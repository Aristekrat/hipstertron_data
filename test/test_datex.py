import unittest
import sys
import datetime
sys.path.append("../scraper")
from utility import datex

class DatexTestCase(unittest.TestCase):

	def test_convert_to_datetime_against_valid_input(self):
		self.assertEqual(datex.convert_to_datetime(["November 15 2025"]), [datetime.datetime(2025, 11, 15, 0, 0)])

	def test_convert_to_datetime_against_date_in_past(self):
		self.assertEqual(datex.convert_to_datetime(["November 15 2014"]), [None])

	def test_format_months_against_valid_input(self):
		self.assertEqual(datex.format_months(["Oct 15"]), ["October 15"])

	# This one is currently failing
	def test_format_months_against_invalid_input(self):
		self.assertEqual(datex.format_months(["BOOMERANG!", "Oct 15"]), [])

	def test_add_year_against_valid_input(self):
		self.assertEqual(datex.add_year(["October 15"]), ["October 15 2015"])

if __name__ == '__main__':
    unittest.main()