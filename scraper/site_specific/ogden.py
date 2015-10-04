import sys
sys.path.append("..")
from utility import seleniumx, datex, utilityx, ticket_linksx, ticket_pricesx, site_specificx, tracex, soupx
from libraries import selector_library, urls_library

mode = tracex.determine_file_mode()

selectors = selector_library.ogden

urls = urls_library.urls["ogden"]

driver = seleniumx.initialize_driver()

seleniumx.initialize_selenium(urls, driver, "#loadMoreEvents")

tracex.initialize_trace_file(mode, "ogden")


# Artist Section #
artists_raw = seleniumx.selenium_scrape(selectors['artist'], driver)

artists_stripped_chars = utilityx.strip_unwanted_chars(artists_raw)
tracex.create_trace(mode, "ogden", "artists_stripped_chars", artists_stripped_chars)


# Dates Section #
dates_raw = seleniumx.selenium_scrape(selectors['date'], driver)

dates_culled = datex.cull_date_and_month(dates_raw)
tracex.create_trace(mode, "ogden", "dates_culled", dates_culled)

dates_stripped_chars = utilityx.strip_unwanted_chars(dates_culled)
tracex.create_trace(mode, "ogden", "dates_stripped_chars", dates_stripped_chars)

dates_format_month = datex.format_months(dates_stripped_chars)
tracex.create_trace(mode, "ogden", "dates_format_month", dates_format_month)

dates_format_year = datex.add_year(dates_format_month)
tracex.create_trace(mode, "ogden", "dates_format_year", dates_format_year)

dates_datetime = datex.convert_to_datetime(dates_format_year)
tracex.create_trace(mode, "ogden", "dates_datetime", dates_datetime)


# Concert Links Section #
ticket_links_raw = seleniumx.selenium_scrape(selectors["ticket_url"], driver)
tracex.create_trace(mode, "ogden", "ticket_links_raw", ticket_links_raw)

ticket_links = utilityx.lazy_strip(ticket_links_raw, 1)
tracex.create_trace(mode, "ogden", "ticket_links", ticket_links)


# Concert Prices Section #
ticket_prices_raw = soupx.get_results_from_pages(ticket_links, selectors['ticket_price'])
tracex.create_trace(mode, "ogden", "ticket_prices_raw", ticket_prices_raw)

ticket_prices_without_fees = ticket_pricesx.find_prices(ticket_prices_raw)
tracex.create_trace(mode, "ogden", "ticket_prices_without_fees", ticket_prices_without_fees)

ticket_prices = ticket_pricesx.add_fee_estimate(ticket_prices_without_fees)
tracex.create_trace(mode, "ogden", "ticket_prices", ticket_prices)


# DB Function #
utilityx.add_concert_to_database(mode, artists_stripped_chars, dates_datetime, ticket_links, ticket_prices, 3)

print("End of Ogden script reached, exiting.")

seleniumx.end_driver(driver)