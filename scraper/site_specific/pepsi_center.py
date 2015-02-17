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

artists_stripped_html = soupx.strip_html(artists_raw)
tracex.create_trace(mode, "pepsi_center", "artists_stripped_html", artists_stripped_html)

# Had to disable this since Cricket had the gall to put Cricket Presents: in front of the damn artist listing, rather than after
# artists_format_special = site_specificx.pepsi_strip_artists(artists_stripped_html)
# tracex.create_trace(mode, "pepsi_center", "artists_format_special", artists_format_special)


# Dates Section #
dates_raw = soupx.generic_scrape(site_html, selectors["date"])

dates_stripped_html = soupx.strip_html(dates_raw)
tracex.create_trace(mode, "pepsi_center", "dates_stripped_html", dates_stripped_html)

# TODO - create a utility function that finds dates by regex and use it here
dates_format_special = utilityx.remove_listings_without_dates(dates_stripped_html, artists_stripped_html)
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
ticket_links_unfiltered = ticket_linksx.scrape_concert_links(site_html, selectors["ticket_url"])
tracex.create_trace(mode, "pepsi_center", "ticket_links_unfiltered", ticket_links_unfiltered)

ticket_links_filtered = ticket_linksx.filter_urls(ticket_links_unfiltered)
tracex.create_trace(mode, "pepsi_center", "ticket_links_filtered", ticket_links_filtered)

ticket_links = ticket_linksx.remove_duplicates(ticket_links_filtered)
tracex.create_trace(mode, "pepsi_center", "ticket_links", ticket_links)

ticket_links.insert(-1, "javascript:void(0);")
# ticket_links = site_specificx.swift_fix(ticket_links_filtered)
# tracex.create_trace(mode, "pepsi_center", "ticket_links", ticket_links)


# Concert Prices Section #
ticket_pages = soupx.get_pages(ticket_links)

ticket_prices_raw = soupx.generic_scrape(ticket_pages, selectors['ticket_price'])
tracex.create_trace(mode, "pepsi_center", "ticket_prices_raw", ticket_prices_raw)

ticket_prices_html = soupx.strip_html(ticket_prices_raw)
tracex.create_trace(mode, "pepsi_center", "ticket_prices_html", ticket_prices_html)

ticket_prices_without_fees = ticket_linksx.find_prices(ticket_prices_html)
tracex.create_trace(mode, "pepsi_center", "ticket_prices_without_fees", ticket_prices_without_fees)

ticket_prices_patched = ticket_linksx.patch_no_results_found(ticket_prices_raw, ticket_prices_without_fees)
tracex.create_trace(mode, "pepsi_center", "ticket_prices_patched", ticket_prices_patched)

ticket_prices = ticket_linksx.add_fee_estimate(ticket_prices_without_fees)
tracex.create_trace(mode, "pepsi_center", "ticket_prices", ticket_prices)

ticket_prices.insert(-1, 0)


# DB Function #
utilityx.add_concert_to_database(mode, artists_stripped_html, dates_datetime, ticket_links, ticket_prices, 8)

print("End of Pepsi Center script reached, exiting.")