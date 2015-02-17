import unittest
import sys
sys.path.append("../scraper")
sys.path.append("..")
from utility import soupx, datex, utilityx, ticket_linksx, site_specificx 
from libraries import selector_library
from test_helpers import utilityh
from stack_trace import red_rocks_trace

selectors = selector_library.red_rocks
source = open('source/pepsi_center.html')
site_html = utilityh.soup_from_source(source)
artists_raw = soupx.generic_scrape(site_html, selectors["artist"])
dates_raw = soupx.scrape_by_class(site_html, selectors["date"])

class RedRocksTestCase(unittest.TestCase):
	# Length Comparison Tests
	def test_raw_html_list_length(self):
		self.assertEqual(len(artists_raw), len(dates_raw))

	def test_second_transformation_length(self):
		self.assertEqual(len(red_rocks_trace.artists_stripped_html), len(red_rocks_trace.dates_stripped_datechars))

	def test_third_transformation_length(self):
		self.assertEqual(len(red_rocks_trace.artists_stripped_chars), len(red_rocks_trace.dates_culled))

	def test_dates_stripped_chars_length(self):
		self.assertEqual(len(red_rocks_trace.ticket_prices_without_fees), len(red_rocks_trace.artists_stripped_chars))		

	def test_dates_format_year(self):
		self.assertEqual(len(red_rocks_trace.ticket_prices_patched), len(red_rocks_trace.artists_stripped_chars))		

	def test_final_list_length(self):
		self.assertEqual(len(red_rocks_trace.dates_datetime), len(red_rocks_trace.ticket_links), len(red_rocks_trace.ticket_prices))
		self.assertEqual(len(red_rocks_trace.artists_stripped_chars), len(red_rocks_trace.ticket_links), len(red_rocks_trace.ticket_prices))

if __name__ == '__main__':
    unittest.main()
    source.close()