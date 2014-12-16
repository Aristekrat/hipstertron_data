import unittest
import sys
sys.path.append("../scraper")
sys.path.append("..")
from utility import soupx, datex, utilityx, ticket_linksx, site_specificx 
from libraries import selector_library
from test_helpers import utilityh
from stack_trace import fillmore_trace

selectors = selector_library.fillmore

class FillmoreTestCase(unittest.TestCase):
	def setUp(self):
		self.source = open('source/fillmore.html')
		self.site_html = utilityh.soup_from_source(self.source)
		self.artists_raw = soupx.generic_scrape(self.site_html, selectors["artist"])
		self.dates_raw = soupx.generic_scrape(self.site_html, selectors["date"])
	
	# Length Comparison Tests
	def test_raw_html_list_length(self):
		self.assertEqual(len(self.artists_raw), len(self.dates_raw))

	def test_stripped_html_list_length(self):
		self.assertEqual(len(fillmore_trace.artists_stripped_html), len(fillmore_trace.dates_stripped_html))

	def test_dates_stripped_ends_length(self):
		self.assertEqual(len(fillmore_trace.artists_stripped_html), len(fillmore_trace.dates_stripped_ends))

	def test_dates_format_special_length(self):
		self.assertEqual(len(fillmore_trace.artists_stripped_html), len(fillmore_trace.dates_format_special))

	def test_stripped_html_list_length(self):
		self.assertEqual(len(fillmore_trace.artists_stripped_html), len(fillmore_trace.dates_stripped_html))

	def test_ticket_links_relative_length(self):
		self.assertEqual(len(fillmore_trace.artists_stripped_html), len(fillmore_trace.ticket_links_relative))

	def test_final_list_length(self):
		self.assertEqual(len(fillmore_trace.artists_stripped_html), len(fillmore_trace.ticket_links), len(fillmore_trace.dates_datetime))
	
	def tearDown(self):
		self.source.close()

if __name__ == '__main__':
    unittest.main()