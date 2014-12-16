import unittest
import sys
sys.path.append("../scraper")
sys.path.append("..")
from utility import soupx, datex, utilityx, ticket_linksx, site_specificx 
from libraries import selector_library
from test_helpers import utilityh
from stack_trace import pepsi_center_trace

selectors = selector_library.pepsi_center

class PepsiTestCase(unittest.TestCase):
	def setUp(self):
		self.source = open('source/pepsi_center.html')
		self.site_html = utilityh.soup_from_source(self.source)
		self.artists_raw = soupx.generic_scrape(self.site_html, selectors["artist"])
		self.dates_raw = soupx.generic_scrape(self.site_html, selectors["date"])
	
	# Length Comparison Tests
	def test_raw_html_list_length(self):
		self.assertEqual(len(self.artists_raw), len(self.dates_raw))

	def test_second_transformation_length(self):
		self.assertEqual(len(pepsi_center_trace.artists_format_special), len(pepsi_center_trace.dates_format_special))

	def test_dates_culled_length(self):
		self.assertEqual(len(pepsi_center_trace.artists_format_special), len(pepsi_center_trace.dates_culled))

	def test_dates_stripped_chars_length(self):
		self.assertEqual(len(pepsi_center_trace.artists_format_special), len(pepsi_center_trace.dates_stripped_chars))		

	def test_dates_format_year(self):
		self.assertEqual(len(pepsi_center_trace.artists_format_special), len(pepsi_center_trace.dates_format_year))		

	def test_final_list_length(self):
		self.assertEqual(len(pepsi_center_trace.artists_format_special), len(pepsi_center_trace.dates_datetime), len(pepsi_center_trace.ticket_links_patched))

	def tearDown(self):
		self.source.close()

if __name__ == '__main__':
    unittest.main()