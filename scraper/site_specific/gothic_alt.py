import sys
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx, showlinkx, site_specificx, selector_library, urls_library
from selenium import webdriver
from time import sleep

selectors = selector_library.gothic

urls = urls_library.urls["gothic"]

site_html = sitex.get_pages(urls)

chrome = webdriver.PhantomJS()

chrome.get(urls[0])

button = chrome.find_element_by_css_selector("#loadMoreEvents")

actions = webdriver.common.action_chains.ActionChains(chrome)

actions.move_to_element(button)
actions.click(button)
actions.perform()

sleep(2)

actions.click(button)
actions.perform()


# Artist Section #
artists_stripped_html = sitex.selenium_scrape(selectors['artist'], chrome)

artists_stripped = utilityx.strip_unwanted_chars(artists_stripped_html)


# Dates Section #
dates_html = sitex.selenium_scrape(selectors['date'], chrome)

dates_stripped_html = datex.cull_date_and_month(dates_html)

dates_stripped_datechars = utilityx.strip_unwanted_chars(dates_stripped_html)

dates_formatted_month = datex.format_months(dates_stripped_datechars)

dates_formatted_year = datex.add_year(dates_formatted_month)

dates_datetime = datex.convert_to_datetime(dates_formatted_year)


# Concert Links Section #
concert_details_html = sitex.selenium_scrape('.buttons', chrome)

concert_details_links = utilityx.lazy_scrape(concert_details_html, 1)


# DB Function #
utilityx.add_concert_to_database(artists_stripped, dates_datetime, concert_details_links, 1)

chrome.close()