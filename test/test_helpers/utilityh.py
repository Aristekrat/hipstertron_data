import unittest

def test_not_empty (context, results):
	for result in results: 
		if (result == None):
			context.fail()