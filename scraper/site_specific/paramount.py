import sys
sys.path.append("..")
from utility import seleniumx, datex, utilityx, ticket_linksx, site_specificx, tracex, soupx
from libraries import selector_library, urls_library

mode = tracex.determine_file_mode()

selectors = selector_library.paramount

urls = urls_library.urls["paramount"]

driver = seleniumx.initialize_driver()

seleniumx.initialize_selenium(urls, driver, "#btn-MoreEvents")

tracex.initialize_trace_file(mode, "paramount")


# Artist Section #
artists_raw = seleniumx.selenium_scrape(selectors['artist'], driver)

artists_stripped_chars = utilityx.strip_unwanted_chars(artists_raw)
tracex.create_trace(mode, "paramount", "artists_stripped_chars", artists_stripped_chars)


# Dates Section #
dates_raw = seleniumx.selenium_scrape(selectors['date'], driver)

dates_culled = datex.cull_date_and_month(dates_raw)
tracex.create_trace(mode, "paramount", "dates_culled", dates_culled)

dates_stripped_chars = utilityx.strip_unwanted_chars(dates_culled)
tracex.create_trace(mode, "paramount", "dates_stripped_chars", dates_stripped_chars)

dates_format_month = datex.format_months(dates_stripped_chars)
tracex.create_trace(mode, "paramount", "dates_format_month", dates_format_month)

dates_format_year = datex.add_year(dates_format_month)
tracex.create_trace(mode, "paramount", "dates_format_year", dates_format_year)

dates_datetime = datex.convert_to_datetime(dates_format_year)
tracex.create_trace(mode, "paramount", "dates_datetime", dates_datetime)


# Ticket Links Section #
ticket_links_raw = seleniumx.selenium_scrape(selectors["ticket_url"], driver)
tracex.create_trace(mode, "paramount", "ticket_links_raw", ticket_links_raw)

ticket_links_relative = ticket_linksx.scrape_hrefs(ticket_links_raw)
tracex.create_trace(mode, "paramount", "ticket_links_relative", ticket_links_relative)

ticket_links = ticket_linksx.ticket_link_prefix("http://www.altitudetickets.com", ticket_links_relative)
tracex.create_trace(mode, "paramount", "ticket_links", ticket_links)


# Concert Prices Section #
ticket_pages = soupx.get_pages(ticket_links)

ticket_prices_raw = soupx.generic_scrape(ticket_pages, selectors['ticket_price'])

ticket_prices_without_fees = ticket_linksx.find_prices(ticket_prices_raw)
tracex.create_trace(mode, "paramount", "ticket_prices_without_fees", ticket_prices_without_fees)

ticket_prices_patched = ticket_linksx.patch_no_results_found(ticket_prices_raw, ticket_prices_without_fees)
tracex.create_trace(mode, "paramount", "ticket_prices_patched", ticket_prices_patched)

ticket_prices = ticket_linksx.add_fee_estimate(ticket_prices_patched)
tracex.create_trace(mode, "paramount", "ticket_prices", ticket_prices)


# DB Function #
utilityx.add_concert_to_database(mode, artists_stripped_chars, dates_datetime, ticket_links, ticket_prices, 7)

print("End of Paramount Theater script reached, exiting.")

seleniumx.end_driver(driver)
