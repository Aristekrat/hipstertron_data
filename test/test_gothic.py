import unittest
import sys
from selenium import webdriver
sys.path.append("../scraper")
sys.path.append("..")
from utility import seleniumx, datex, utilityx, ticket_linksx
from libraries import selector_library
from test_helpers import utilityh, dateh
from stack_trace import gothic_trace

selectors = selector_library.gothic

driver = webdriver.PhantomJS()

driver.get("source/gothic.html")

# Putting these two in setup slows down the test too much.
artists_raw = seleniumx.selenium_scrape(selectors['artist'], driver)
dates_raw = seleniumx.selenium_scrape(selectors['date'], driver)

class GothicTestCase(unittest.TestCase):
	# Length Comparison Tests
	def test_raw_html_list_length(self):
		self.assertEqual(len(artists_raw), len(dates_raw), len(gothic_trace.ticket_links_raw))

	def test_second_transformation_length(self):
		self.assertEqual(len(gothic_trace.artists_stripped_chars), len(gothic_trace.dates_culled))

	def test_dates_stripped_chars_length(self):
		self.assertEqual(len(gothic_trace.artists_stripped_chars), len(gothic_trace.dates_stripped_chars))

	def test_dates_format_month_length(self):
		self.assertEqual(len(gothic_trace.artists_stripped_chars), len(gothic_trace.dates_format_year))

	def test_dates_format_year_length(self):
		self.assertEqual(len(gothic_trace.artists_stripped_chars), len(gothic_trace.dates_format_year))

	def test_final_list_length(self):
		self.assertEqual(len(gothic_trace.artists_stripped_chars), len(gothic_trace.dates_datetime), len(gothic_trace.ticket_links))

if __name__ == '__main__':
	unittest.main()
	driver.close()