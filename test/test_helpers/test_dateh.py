import unittest
import dateh

#This test suite primarily works through passing bad inputs to figure out if the helper functions will detect them
class DatehTestCase(unittest.TestCase):

	#When the decorator is active, it will raise an error if the test unexpectedly passed. It also supresses both the failure message and warning
	@unittest.expectedFailure 
	def test_cull_date_and_month_helper(self):
		dateh.test_cull_date_and_month(self, ["Nonsense", "More Nonsense"])
		dateh.test_cull_date_and_month(self, ["November December"])

	@unittest.expectedFailure 
	def test_format_month_helper(self):
		dateh.test_format_month(self, ["13 November 2014"])

if __name__ == '__main__':
    unittest.main()