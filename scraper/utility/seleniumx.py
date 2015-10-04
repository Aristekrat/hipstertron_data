from selenium import webdriver
from time import sleep

# I was almost able to initialize the driver here and eliminate passing it in to subsequent functions.
# However, it caused an error when another selenium script ran. There has to be a way to initialize here and then end it here at appropriate times. 
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

# Initializes Selenium. Not usable other than clicking buttons and pages without buttons. 
def initialize_selenium(urls, driver, selector=None):
	driver.get(urls[0])

	if (selector):
		button = driver.find_element_by_css_selector(selector)
		actions = webdriver.common.action_chains.ActionChains(driver)

		actions.move_to_element(button)
		actions.click(button)
		actions.perform()

		sleep(2)

		actions.click(button)
		actions.perform()

# Initializes Selenium. Not usable other than clicking buttons and pages without buttons. 
# TODO - follow up on this function, make sure it's fully implemented in place of the less flexible function above
def new_and_better(urls, driver, times=0, selector=None):
	driver.get(urls[0])
	if (selector):
		button = driver.find_element_by_css_selector(selector)
		actions = webdriver.common.action_chains.ActionChains(driver)
		while times > 0:
			actions.move_to_element(button)
			actions.click(button)
			actions.perform()
			sleep(5)
			times = times - 1

def end_driver(driver):
	driver.close()