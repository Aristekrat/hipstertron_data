import sys
sys.path.append("..")
from utility import seleniumx, datex, utilityx, ticket_linksx,  tracex 
from libraries import selector_library, urls_library

mode = tracex.determine_file_mode()

selectors = selector_library.bluebird

urls = urls_library.urls["bluebird"]

driver = seleniumx.initialize_driver()

seleniumx.initialize_selenium(urls, driver, "#loadMoreEvents")

tracex.initialize_trace_file(mode, "bluebird")

# Artist Section #
artists_raw = seleniumx.selenium_scrape(selectors['artist'], driver)

artists_stripped_chars = utilityx.strip_unwanted_chars(artists_raw)
tracex.create_trace(mode, "bluebird", "artists_stripped_chars", artists_stripped_chars)


# Dates Section #
dates_raw = seleniumx.selenium_scrape(selectors['date'], driver)

dates_culled = datex.cull_date_and_month(dates_raw)
tracex.create_trace(mode, "bluebird", "dates_culled", dates_culled)

dates_stripped_chars = utilityx.strip_unwanted_chars(dates_culled)
tracex.create_trace(mode, "bluebird", "dates_stripped_chars", dates_stripped_chars)

dates_format_month = datex.format_months(dates_stripped_chars)
tracex.create_trace(mode, "bluebird", "dates_format_month", dates_format_month)

dates_format_year = datex.add_year(dates_format_month)
tracex.create_trace(mode, "bluebird", "dates_format_year", dates_format_year)

dates_datetime = datex.convert_to_datetime(dates_format_year)
tracex.create_trace(mode, "bluebird", "dates_datetime", dates_datetime)

# Concert Links Section #
ticket_links_raw = seleniumx.selenium_scrape(selectors['ticket_url'], driver)
tracex.create_trace(mode, "bluebird", "ticket_links_raw", ticket_links_raw)

ticket_links = utilityx.lazy_strip(ticket_links_raw, 1)
tracex.create_trace(mode, "bluebird", "ticket_links", ticket_links)

# DB Function #
utilityx.add_concert_to_database(mode, artists_stripped_chars, dates_datetime, ticket_links, 2)

print("End of Bluebird script reached, exiting.")

seleniumx.end_driver(driver)