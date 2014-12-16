import unittest
from bs4 import BeautifulSoup
from selenium import webdriver

def test_not_empty (context, results):
	if results == []:
		print("Failed because list is empty")
		context.fail()
	for result in results: 
		if (result == None or result == ''):
			print("Failed because 'None' value present in list or one of the values was an empty string")
			context.fail()

def soup_from_source (source):
	soup_page = []
	soupified = BeautifulSoup(source)
	soup_page.append(soupified)
	return soup_page