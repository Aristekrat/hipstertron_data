import sys
sys.path.append("../../scraper")
sys.path.append("../..")
from selenium import webdriver
from utility import seleniumx 
from libraries import urls_library

target = sys.argv[1]

root_url = urls_library.urls[target]

driver = webdriver.PhantomJS()

seleniumx.initialize_selenium(root_url, driver)

write_file = target + ".html"

source = open(write_file, 'w')

source.write(str(driver.page_source))

source.close()

driver.close()