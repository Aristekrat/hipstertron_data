import sys
sys.path.append("..")
from utility import soupx, datex, utilityx, ticket_linksx, site_specificx, tracex
from libraries import selector_library, urls_library

mode = tracex.determine_file_mode()

urls = urls_library.urls["pepsi_center"]

selectors = selector_library.pepsi_center

site_html = soupx.get_pages(urls)

tracex.initialize_trace_file(mode, "pepsi_center")


# Artist Section #
artists_raw = soupx.generic_scrape(site_html, selectors["artist"])

artists_stripped_html = utilityx.strip_html(artists_raw)
tracex.create_trace(mode, "pepsi_center", "artists_stripped_html", artists_stripped_html)

artists_format_special = site_specificx.pepsi_strip_artists(artists_stripped_html)
tracex.create_trace(mode, "pepsi_center", "artists_format_special", artists_format_special)


# Dates Section #
dates_raw = soupx.generic_scrape(site_html, selectors["date"])

dates_stripped_html = utilityx.strip_html(dates_raw)
tracex.create_trace(mode, "pepsi_center", "dates_stripped_html", dates_stripped_html)

# TODO - create a utility function that finds dates by regex and use it here
dates_format_special = utilityx.remove_listings_without_dates(dates_stripped_html, artists_format_special)
tracex.create_trace(mode, "pepsi_center", "dates_format_special", dates_format_special)

dates_culled = datex.cull_date_and_month(dates_format_special)
tracex.create_trace(mode, "pepsi_center", "dates_culled", dates_culled)

dates_stripped_chars = utilityx.strip_unwanted_chars(dates_culled)
tracex.create_trace(mode, "pepsi_center", "dates_stripped_chars", dates_stripped_chars)

dates_format_year = datex.add_year(dates_stripped_chars)
tracex.create_trace(mode, "pepsi_center", "dates_format_year", dates_format_year)

dates_datetime = datex.convert_to_datetime(dates_format_year)
tracex.create_trace(mode, "pepsi_center", "dates_datetime", dates_datetime)


# Show Links Section #
ticket_links = ticket_linksx.scrape_concert_links(site_html, selectors["ticket_url"])
tracex.create_trace(mode, "pepsi_center", "ticket_links", ticket_links)

ticket_links_patched = ticket_linksx.lazy_links_patch(artists_format_special, ticket_links)
tracex.create_trace(mode, "pepsi_center", "ticket_links_patched", ticket_links_patched)


# DB Function #
utilityx.add_concert_to_database(mode, artists_format_special, dates_datetime, ticket_links_patched, 8)

print("End of Pepsi Center script reached, exiting.")