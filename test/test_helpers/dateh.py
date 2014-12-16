import unittest
import re
import warnings

# All dates should have a defined format by the time they're ready to be converted:
# Month, day, year. Create a function that splits the string and tests each component to see if matches what it is supposed to

# Appears to work
def break_into_components(context, results):
	atomic = []
	for result in results:
		components = result.split()
		atomic.append(components)
	return atomic

# Write function : tests month

# Write function : tests day

# Write function : tests year

# Write function : tests the whole thing, and that the component list is only 3 long

# Haven't tested this test function yet
def test_format_month(context, results):
	for result in results:
		components = result.split()
		x = re.search('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec', components[0])
		context.assertIsNotNone(x)

def test_cull_date_and_month(context, results):
	month_matcher = re.compile('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec')
	for index, result in enumerate(results):
		x = month_matcher.findall(result)
		if (x == []):
			context.fail("No month found in result at index: {0}".format(index))
		elif(len(x) > 1):
			warnings.warn("Warning - two results found!", RuntimeWarning)