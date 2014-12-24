import sys
sys.path.append("..")
from utility import soupx, datex, utilityx, ticket_linksx, site_specificx, tracex
from libraries import selector_library, urls_library

mode = tracex.determine_file_mode()

selectors = selector_library.red_rocks

urls = urls_library.urls["red_rocks"]

site_html = soupx.get_pages(urls)

tracex.initialize_trace_file(mode, "red_rocks")


# Artist Section #
artists_raw = soupx.generic_scrape(site_html, selectors["artist"])

artists_stripped_html = soupx.strip_html(artists_raw)
tracex.create_trace(mode, "red_rocks", "artists_stripped_html", artists_stripped_html)

artists_stripped_chars = utilityx.strip_string_ends(artists_stripped_html, 0, 10)
tracex.create_trace(mode, "red_rocks", "artists_stripped_chars", artists_stripped_chars)


# Dates Section #
# Redrocks doesn't include the concert dates in plain text, so I have to harvest the concert details,
# go to that page, and then get the date. This is the first step, link harvesting. 
date_urls = ticket_linksx.scrape_links_from_result_set(artists_raw)

date_pages = soupx.get_pages(date_urls)

dates_html = soupx.scrape_by_class(date_pages, selectors["date"])

dates_stripped_html = soupx.strip_html(dates_html)
tracex.create_trace(mode, "red_rocks", "dates_stripped_html", dates_stripped_html)

dates_stripped_datechars = utilityx.strip_unwanted_chars(dates_stripped_html)
tracex.create_trace(mode, "red_rocks", "dates_stripped_datechars", dates_stripped_datechars)

dates_culled = datex.cull_date_and_month(dates_stripped_datechars)
tracex.create_trace(mode, "red_rocks", "dates_culled", dates_culled)

dates_format_year = datex.add_year(dates_culled)
tracex.create_trace(mode, "red_rocks", "dates_format_year", dates_format_year)

dates_datetime = datex.convert_to_datetime(dates_format_year)
tracex.create_trace(mode, "red_rocks", "dates_datetime", dates_datetime)


# Show Links Section #
ticket_links = ticket_linksx.scrape_concert_links(site_html, selectors["ticket_url"])
tracex.create_trace(mode, "red_rocks", "ticket_links", ticket_links)


# DB Function #
utilityx.add_concert_to_database(mode, artists_stripped_chars, dates_datetime, ticket_links, 9)

print("End of Red Rocks script reached, exiting.")