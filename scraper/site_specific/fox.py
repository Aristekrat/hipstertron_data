import sys
sys.path.append("..")
from utility import seleniumx, datex, utilityx, ticket_linksx, site_specificx, tracex, soupx
from libraries import selector_library, urls_library
from selenium import webdriver

mode = tracex.determine_file_mode()

selectors = selector_library.fox

urls = urls_library.urls["fox"]

driver = seleniumx.initialize_driver()

seleniumx.initialize_selenium(urls, driver)

tracex.initialize_trace_file(mode, "fox")

# Artist Section #
artists_raw = seleniumx.selenium_scrape(selectors['artist'], driver)

artists_stripped_chars = utilityx.strip_unwanted_chars(artists_raw)
# Note - the list still represents &s as &amp, but apparently that's harmless, it'll be converted when redisplayed. UPDATE, not actually true :-(
tracex.create_trace(mode, "fox", "artists_stripped_chars", artists_stripped_chars)

artists_format_capitalization = utilityx.correct_capitalization(artists_stripped_chars)
tracex.create_trace(mode, "fox", "artists_format_capitalization", artists_format_capitalization)


# Dates Section #
dates_month = seleniumx.selenium_scrape(selectors['month'], driver)
tracex.create_trace(mode, "fox", "dates_month", dates_month)

dates_day = seleniumx.selenium_scrape(selectors['day'], driver)
tracex.create_trace(mode, "fox", "dates_day", dates_day)

dates_combined = site_specificx.combine(dates_month, dates_day)
tracex.create_trace(mode, "fox", "dates_combined", dates_combined)

dates_format_month = datex.format_months(dates_combined)
tracex.create_trace(mode, "fox", "dates_format_month", dates_format_month)

dates_format_year = datex.add_year(dates_format_month)
tracex.create_trace(mode, "fox", "dates_format_year", dates_format_year)

dates_datetime = datex.convert_to_datetime(dates_format_year)
tracex.create_trace(mode, "fox", "dates_datetime", dates_datetime)


# Ticket Links Section #
ticket_links_raw = seleniumx.selenium_scrape(selectors["ticket_url"], driver)
tracex.create_trace(mode, "fox", "ticket_links_raw", ticket_links_raw)

ticket_links_relative = utilityx.lazy_strip(ticket_links_raw, 5)
tracex.create_trace(mode, "fox", "ticket_links_relative", ticket_links_relative)

ticket_links = ticket_linksx.ticket_link_prefix("http://foxtheatre.com", ticket_links_relative)
tracex.create_trace(mode, "fox", "ticket_links", ticket_links)


# Concert Prices Section #
ticket_prices = ticket_linksx.no_prices(ticket_links)

# Fox still can't be parsed with BS4
# ticket_pages = soupx.get_pages(ticket_links)

# ticket_prices_raw = soupx.generic_scrape(ticket_pages, selectors['ticket_price'])
# tracex.create_trace(mode, "fox", "ticket_prices_raw", ticket_prices_raw)

# ticket_prices_html = soupx.strip_html(ticket_prices_raw)
# tracex.create_trace(mode, "fox", "ticket_prices_html", ticket_prices_html)

# ticket_prices_without_fees = ticket_linksx.find_prices(ticket_prices_html)
# tracex.create_trace(mode, "fox", "ticket_prices_without_fees", ticket_prices_without_fees)

# ticket_prices = ticket_linksx.add_fee_estimate(ticket_prices_without_fees)
# tracex.create_trace(mode, "fox", "ticket_prices", ticket_prices)


# DB Function #
utilityx.add_concert_to_database(mode, artists_format_capitalization, dates_datetime, ticket_links, ticket_prices, 10)

print("End of Fox Theater script reached, exiting.")

seleniumx.end_driver(driver)