import unittest
import sys
from selenium import webdriver
sys.path.append("../scraper")
sys.path.append("..")
from utility import seleniumx
from libraries import selector_library
from stack_trace import fox_trace

selectors = selector_library.fox

driver = webdriver.PhantomJS()

driver.get("source/fox.html")

# Putting these two in setup slows down the test too much.
artists_raw = seleniumx.selenium_scrape(selectors['artist'], driver)
dates_raw = seleniumx.selenium_scrape(selectors['date'], driver)

class FoxTestCase(unittest.TestCase):
	# Length Comparison Tests
	def test_first_step_length(self):
		self.assertEqual(len(fox_trace.artists_stripped_chars), len(fox_trace.dates_combined), len(fox_trace.ticket_links_raw))

	def test_dates_format_month_length(self):
		self.assertEqual(len(fox_trace.artists_format_capitalization), len(fox_trace.dates_format_month))

	def test_dates_format_year_length(self):
		self.assertEqual(len(fox_trace.artists_format_capitalization), len(fox_trace.dates_format_year))

	def test_ticket_links_raw_length(self):
		self.assertEqual(len(fox_trace.artists_format_capitalization), len(fox_trace.ticket_links_raw))

	def test_ticket_links_raw_length(self):
		self.assertEqual(len(fox_trace.artists_format_capitalization), len(fox_trace.ticket_links_relative))

	def test_final_list_length(self):
		self.assertEqual(len(fox_trace.artists_format_capitalization), len(fox_trace.dates_datetime), len(fox_trace.ticket_links))

if __name__ == '__main__':
	unittest.main()
	driver.close()