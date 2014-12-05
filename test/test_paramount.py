import unittest
import sys
sys.path.append("../scraper")
sys.path.append("..")
from utility import sitex, datex, utilityx, showlinkx, selector_library, urls_library, site_specificx
from test_helpers import utilityh

selectors = selector_library.paramount

urls = urls_library.urls["paramount"]

class GothicTestCase(unittest.TestCase):

	def setUp(self):
		self.site_html = sitex.get_pages(urls)
		self.artists_html = artistx.scrape_artists(self.site_html, selectors['artist'])
		self.dates_html = datex.scrape_dates(self.site_html, selectors['date'])

	# Artist Section
	def test_artists_raw_html(self):
		utilityh.test_not_empty(self, self.artists_html)

	def test_artists_stripped_html(self):
		self.artists_stripped_html = utilityx.strip_html(self.artists_html)
		utilityh.test_not_empty(self, self.artists_stripped_html)

	def test_artists_stripped_chars(self):
		self.artists_stripped_html = utilityx.strip_html(self.artists_html)
		self.artists_stripped_chars = utilityx.strip_unwanted_chars(self.artists_stripped_html)
		utilityh.test_not_empty(self, self.artists_stripped_chars)

	# Dates Section
	def test_dates_raw_html(self):
		utilityh.test_not_empty(self, self.dates_html)

	def test_dates_stripped_html(self):
		self.dates_stripped_html = site_specificx.special_strip_html(self.dates_html)
		utilityh.test_not_empty(self, self.dates_stripped_html)

	def test_dates_stripped_datechars(self):
		self.dates_stripped_html = site_specificx.special_strip_html(self.dates_html)
		self.dates_stripped_datechars = utilityx.strip_unwanted_chars(self.dates_stripped_html)
		utilityh.test_not_empty(self, self.dates_stripped_datechars)



if __name__ == '__main__':
    unittest.main()