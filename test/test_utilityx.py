import unittest
import sys
sys.path.append("../scraper")
sys.path.append("..")
from utility import utilityx

class UtilityxTestCase(unittest.TestCase):

	def test_strip_string_ends(self):
		self.assertEqual(utilityx.strip_string_ends(["oFooo", "Foooooooooooo", "BMooo"], 1, 1), ["Foo", "ooooooooooo", "Moo"])
		self.assertEqual(utilityx.strip_string_ends(["Foooo", "Foooooooooooo", "BMooo"], 0, 4), ["F", "Foooooooo", "B"])

	def test_strip_unwanted_chars(self):
		self.assertEqual(utilityx.strip_unwanted_chars(["foo\n", "foo\t", "foo,", "foo."]), ["foo", "foo", "foo", "foo"])

	def test_correct_capitalization(self):
		self.assertEqual(utilityx.correct_capitalization(["foo", "FOO", "fOO"]), ["Foo", "Foo", "Foo"])

	def test_lazy_strip(self):
		result_set = ['Mary had a "little lamb" whose fleece was white as "snow" and everywhere that Mary "went" the lamb would surely go.']
		self.assertEqual(utilityx.lazy_strip(result_set, 1), ["little lamb"])
		self.assertEqual(utilityx.lazy_strip(result_set, -2), ["went"])
		self.assertEqual(utilityx.lazy_strip(result_set, 3), ["snow"])
	
	def test_remove_listings_without_dates(self):
		dates = ["Dec 12", "Biff", None, 5, "1232111", "8 Mar", ""]
		artists = ["Foo", "Foo", "Foo", "Foo", "Foo", "Foo", "Foo"]
		self.assertEqual(len(artists), len(dates), 2)

if __name__ == '__main__':
    unittest.main()