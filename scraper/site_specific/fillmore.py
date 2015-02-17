import sys
sys.path.append("..")
from utility import soupx, datex, utilityx, ticket_linksx, tracex, site_specificx
from libraries import selector_library, urls_library

mode = tracex.determine_file_mode()

root_url = urls_library.urls["fillmore"]

selectors = selector_library.fillmore

tracex.initialize_trace_file(mode, "fillmore")


# URL Harvest #
root = soupx.get_pages(root_url)

urls = site_specificx.scrape_concert_pages(root, root_url, selectors["page_url"])

site_html = soupx.get_pages(urls)


# Artist Section #
artists_raw = soupx.generic_scrape(site_html, selectors["artist"])

artists_stripped_html = soupx.strip_html(artists_raw)
tracex.create_trace(mode, "fillmore", "artists_stripped_html", artists_stripped_html)


# Dates Section #
dates_raw = soupx.generic_scrape(site_html, selectors["date"])

dates_stripped_html = soupx.strip_html(dates_raw)
tracex.create_trace(mode, "fillmore", "dates_stripped_html", dates_stripped_html)

#TODO - create a function that can strip times based on regex
dates_stripped_ends = utilityx.strip_string_ends(dates_stripped_html, 0, 9)
tracex.create_trace(mode, "fillmore", "dates_stripped_ends", dates_stripped_ends)

dates_format_special = datex.move_date_behind_month(dates_stripped_ends)
tracex.create_trace(mode, "fillmore", "dates_format_special", dates_format_special)

dates_datetime = datex.convert_to_datetime(dates_format_special)
tracex.create_trace(mode, "fillmore", "dates_datetime", dates_datetime)


# Ticket Links Section #
ticket_links_relative = ticket_linksx.scrape_concert_links(site_html, selectors["ticket_url"])
tracex.create_trace(mode, "fillmore", "ticket_links_relative", ticket_links_relative)

ticket_links = ticket_linksx.ticket_link_prefix("http://www.fillmoreauditorium.org", ticket_links_relative)
tracex.create_trace(mode, "fillmore", "ticket_links", ticket_links)


# Concert Prices Section #
ticket_prices = ticket_linksx.no_prices(ticket_links)
tracex.create_trace(mode, "fillmore", "ticket_prices", ticket_prices)


# DB Function #
utilityx.add_concert_to_database(mode, artists_stripped_html, dates_datetime, ticket_links, ticket_prices, 4)

print("End of Fillmore script reached, exiting.")