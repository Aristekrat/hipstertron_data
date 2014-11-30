import sys
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx, showlinkx, site_specificx, selector_library, urls_library

root_url = urls_library.urls["fillmore"]

selectors = selector_library.fillmore

# URL Harvest #
root = sitex.get_pages(root_url)

urls = site_specificx.scrape_concert_pages(root, root_url, selectors["page_url"])

site_html = sitex.get_pages(urls)


# Artist Section #
artists_html = artistx.scrape_artists(site_html, selectors["artist"])

artists_stripped = utilityx.strip_html(artists_html)


# Dates Section #
dates_html = datex.scrape_dates(site_html, selectors["date"])

dates_stripped_html = utilityx.strip_html(dates_html)

dates_stripped_datechars = utilityx.strip_unwanted_chars(dates_stripped_html)

dates_stripped_ends = utilityx.strip_string_ends(dates_stripped_datechars, 0, 9)

dates_special_mod1 = datex.move_date_behind_month(dates_stripped_ends)

dates_datetime = datex.convert_to_datetime(dates_special_mod1)


# Show Links Section #
concert_details_html = showlinkx.scrape_concert_links(site_html, selectors["ticket_url"])


# DB Function #
utilityx.add_concert_to_database(artists_stripped, dates_datetime, concert_details_html, 4)