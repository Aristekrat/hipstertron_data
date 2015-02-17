import unittest
import sys
sys.path.append("../scraper")
sys.path.append("..")
from utility import soupx, datex, utilityx, ticket_linksx, site_specificx 
from libraries import selector_library
from test_helpers import utilityh
from stack_trace import fillmore_trace

selectors = selector_library.fillmore
source = open('source/fillmore.html')
site_html = utilityh.soup_from_source(source)
artists_raw = soupx.generic_scrape(site_html, selectors["artist"])
dates_raw = soupx.generic_scrape(site_html, selectors["date"])

class FillmoreTestCase(unittest.TestCase):	
	# Length Comparison Tests
	def test_raw_html_list_length(self):
		self.assertEqual(len(artists_raw), len(dates_raw))

	def test_stripped_html_list_length(self):
		self.assertEqual(len(fillmore_trace.artists_stripped_html), len(fillmore_trace.dates_stripped_html))

	def test_dates_stripped_ends_length(self):
		self.assertEqual(len(fillmore_trace.artists_stripped_html), len(fillmore_trace.dates_stripped_ends))

	def test_dates_format_special_length(self):
		self.assertEqual(len(fillmore_trace.artists_stripped_html), len(fillmore_trace.dates_format_special))

	def test_ticket_links_relative_length(self):
		self.assertEqual(len(fillmore_trace.artists_stripped_html), len(fillmore_trace.ticket_links_relative))

	def test_final_list_length(self):
		self.assertEqual(len(fillmore_trace.artists_stripped_html), len(fillmore_trace.ticket_links), len(fillmore_trace.dates_datetime))

if __name__ == '__main__':
    unittest.main()
    source.close()