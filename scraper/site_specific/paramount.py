import sys
sys.path.append("..")
from utility import soupx, datex, utilityx, ticket_linksx, site_specificx, tracex
from libraries import selector_library, urls_library

mode = tracex.determine_file_mode()

selectors = selector_library.paramount

urls = urls_library.urls["paramount"]

site_html = soupx.get_pages(urls)

tracex.initialize_trace_file(mode, "paramount")


#Artist Section#
artists_raw = soupx.generic_scrape(site_html, selectors["artist"])

artists_stripped_html = soupx.strip_html(artists_raw)
tracex.create_trace(mode, "paramount", "artists_stripped_html", artists_stripped_html)


#Dates Section#
dates_raw = soupx.generic_scrape(site_html, selectors["date"])

dates_stripped_html = soupx.strip_html(dates_raw[0])
tracex.create_trace(mode, "paramount", "dates_stripped_html", dates_stripped_html)

dates_culled = datex.cull_date_and_month(dates_stripped_html) #Not quite sure why paramount is pulling down something different
tracex.create_trace(mode, "paramount", "dates_culled", dates_culled)

dates_stripped_chars = utilityx.strip_unwanted_chars(dates_culled)
tracex.create_trace(mode, "paramount", "dates_stripped_chars", dates_stripped_chars)

dates_format_year = datex.add_year(dates_stripped_chars)
tracex.create_trace(mode, "paramount", "dates_format_year", dates_format_year)

dates_datetime = datex.convert_to_datetime(dates_format_year)
tracex.create_trace(mode, "paramount", "dates_datetime", dates_datetime)


#Show Links Section#
ticket_links = ticket_linksx.scrape_concert_links(site_html, selectors["ticket_url"])
tracex.create_trace(mode, "paramount", "ticket_links", ticket_links)


# DB Function #
utilityx.add_concert_to_database(mode, artists_stripped_html, dates_datetime, ticket_links, 7)

print("End of Paramount script reached, exiting.")