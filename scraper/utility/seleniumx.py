from selenium import webdriver
from time import sleep

# I was almost able to initialize the driver here and eliminate passing it in to subsequent functions.
# However, it caused an error when another selenium script ran. There has to be a way to initialize here and then end it here
# At appropriate times. 
def initialize_driver():
	driver = webdriver.PhantomJS()
	return driver

# Scrapes pretty much any data type via selenium
def selenium_scrape(selector, driver):
	stripped = []
	t = driver.find_elements_by_css_selector(selector)
	for result in t:
		stripped.append(result.get_attribute('innerHTML'))
	return stripped

# Initializes selenium for Ogden, First Bank, Gothic, and Bluebird. Someday, it will need to be rewritten for more flexibility. 
def initialize_selenium(urls, driver):
	driver.get(urls[0])
	button = driver.find_element_by_css_selector("#loadMoreEvents")
	actions = webdriver.common.action_chains.ActionChains(driver)

	actions.move_to_element(button)
	actions.click(button)
	actions.perform()

	sleep(2)

	actions.click(button)
	actions.perform()

def simple_initialize(urls, driver):
	driver.get(urls[0])

def end_driver(driver):
	driver.close()