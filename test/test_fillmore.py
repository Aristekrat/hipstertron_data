import unittest
import sys
sys.path.append("../scraper")
sys.path.append("..")
from utility import sitex, datex, utilityx, showlinkx, site_specificx 
from libraries import urls_library, selector_library
from test_helpers import utilityh

#It'd be very good to load the raw html input into a file and pull it from there. I could set up seperate tests for those functions. Pulling it from the site each time is slow.

selectors = selector_library.fillmore

urls = urls_library.urls["fillmore"]

class GothicTestCase(unittest.TestCase):

	def setUp(self):
		self.site_html = sitex.get_pages(urls)
		self.artists_html = sitex.generic_scrape(self.site_html, selectors['artist'])
		self.artists_stripped_html = utilityx.strip_html(self.artists_html)
		self.dates_html = sitex.generic_scrape(self.site_html, selectors['date'])
		self.dates_stripped_html = utilityx.strip_html(self.dates_html)
	
	# Length Comparison Tests
	def test_raw_html_list_length(self):
		self.assertEqual(len(self.artists_html), len(self.dates_html))

	def test_stripped_html_list_length(self):
		self.assertEqual(len(self.artists_stripped_html), len(self.dates_stripped_html))

	# Artist Section
	def test_artists_raw_html(self):
		utilityh.test_not_empty(self, self.artists_html)

	def test_artists_stripped_html(self):
		utilityh.test_not_empty(self, self.artists_stripped_html)

	# Dates Section
	def test_dates_raw_html(self):
		utilityh.test_not_empty(self, self.dates_html)

	def test_dates_stripped_html(self):
		utilityh.test_not_empty(self, self.dates_stripped_html)

	def test_dates_stripped_ends(self):
		# The -1 argument at the end clips off the last character. This is necessary because the function won't accept an argument of 0
		self.dates_stripped_ends = utilityx.strip_string_ends(self.dates_stripped_html, -9, 1)
		# 1
		utilityh.test_not_empty(self, self.dates_stripped_ends)
		# 2
		self.assertEqual(len(self.dates_stripped_ends), len(self.dates_stripped_html))
		# 3
		print("Strip String Ends is removing these characters: {0}".format(self.dates_stripped_ends))


	# def test_dates_stripped_html(self):
	# 	self.dates_stripped_html = site_specificx.special_strip_html(self.dates_html)
	# 	utilityh.test_not_empty(self, self.dates_stripped_html)

	# def test_dates_stripped_datechars(self):
	# 	self.dates_stripped_html = site_specificx.special_strip_html(self.dates_html)
	# 	self.dates_stripped_datechars = utilityx.strip_unwanted_chars(self.dates_stripped_html)
	# 	utilityh.test_not_empty(self, self.dates_stripped_datechars)



if __name__ == '__main__':
    unittest.main()