import unittest
import sys
sys.path.append("../scraper")
sys.path.append("..")
from utility import soupx, datex, utilityx, ticket_linksx, site_specificx 
from libraries import selector_library
from test_helpers import utilityh
from stack_trace import paramount_trace

selectors = selector_library.paramount

class ParamountTestCase(unittest.TestCase):
	def setUp(self):
		# Paramount no longer uses soup.
		self.source = open('source/paramount.html')
		self.site_html = utilityh.soup_from_source(self.source)
		self.artists_raw = soupx.generic_scrape(self.site_html, selectors["artist"])
		self.dates_raw = soupx.generic_scrape(self.site_html, selectors["date"])
	
	# Length Comparison Tests
	def test_raw_html_list_length(self):
		self.assertEqual(len(self.artists_raw), len(self.dates_raw))

	def test_dates_culled_length(self):
		self.assertEqual(len(paramount_trace.artists_stripped_chars), len(paramount_trace.dates_culled))

	def test_dates_stripped_chars_length(self):
		self.assertEqual(len(paramount_trace.artists_stripped_chars), len(paramount_trace.dates_stripped_chars))

	def test_dates_format_month(self):
		self.assertEqual(len(paramount_trace.artists_stripped_chars), len(paramount_trace.dates_format_month))

	def test_dates_format_year(self):
		self.assertEqual(len(paramount_trace.artists_stripped_chars), len(paramount_trace.dates_format_year))

	def test_ticket_links_raw(self):
		self.assertEqual(len(paramount_trace.artists_stripped_chars), len(paramount_trace.ticket_links_raw))

	def test_ticket_links_relative(self):
		self.assertEqual(len(paramount_trace.artists_stripped_chars), len(paramount_trace.ticket_links_relative))

	def test_ticket_links_relative(self):
		self.assertEqual(len(paramount_trace.artists_stripped_chars), len(paramount_trace.ticket_links_relative))
	
	def test_ticket_prices_without_fees(self):
		self.assertEqual(len(paramount_trace.artists_stripped_chars), len(paramount_trace.ticket_prices_without_fees))

	def test_ticket_prices_patched(self):
		self.assertEqual(len(paramount_trace.artists_stripped_chars), len(paramount_trace.ticket_prices_patched))

	def test_final_list_length(self):
		self.assertEqual(len(paramount_trace.dates_datetime), len(paramount_trace.ticket_links), len(paramount_trace.ticket_prices))

	def tearDown(self):
		self.source.close()

if __name__ == '__main__':
    unittest.main()