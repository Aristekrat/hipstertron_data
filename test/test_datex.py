import unittest
import sys
import datetime
sys.path.append("../scraper")
from utility import datex

class DatexTestCase(unittest.TestCase):

	def test_first_conditional_of_cull_date_and_month(self):
		t = datex.cull_date_and_month(["Janury 1", "Feb 3", "April 31", "Tickets Now", None, "November 14", "Nonsense!"])
		self.assertEqual(len(t), 4)

	def test_second_conditional_of_cull_date_and_month(self):
		t = datex.cull_date_and_month(["January 1-5", "January 310"])
		self.assertEqual(t[0], "January 1")
		self.assertEqual(t[1], "January 310") # Not desirable behavior, but currently what I expect

	def test_move_date_behind_month(self):
		self.assertEqual(datex.move_date_behind_month(["12 December 2014"]), ["December 12 2014"])

	def test_convert_to_datetime_against_valid_input(self):
		self.assertEqual(datex.convert_to_datetime(["November 15 2025"]), [datetime.datetime(2025, 11, 15, 0, 0)])

	def test_convert_to_datetime_against_date_in_past(self):
		self.assertEqual(datex.convert_to_datetime(["November 15 2014"]), [None])

	def test_format_months_against_valid_input(self):
		self.assertEqual(datex.format_months(["Oct 15"]), ["October 15"])

	@unittest.expectedFailure
	def test_format_months_against_invalid_input(self):
		self.assertEqual(datex.format_months(["BOOMERANG!", "Oct 15"]), [])

	def test_add_year_against_valid_input(self):
		self.assertEqual(datex.add_year(["October 15"]), ["October 15 2015"])

if __name__ == '__main__':
    unittest.main()