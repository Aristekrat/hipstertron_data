import sys
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx, showlinkx, site_specificx, selector_library, urls_library

selectors = selector_library.firstbank
urls = urls_library.urls["first_bank"]

# URL Harvest #
site_html = sitex.get_pages(urls)

# Artist Section #
artists_html = artistx.scrape_artists(site_html, selectors["artist"])

artists_stripped = utilityx.strip_html(artists_html)


# Dates Section #
dates_html = datex.scrape_dates(site_html, selectors["date"])

dates_stripped_html = site_specificx.special_strip_html(dates_html)

dates_stripped_datechars = utilityx.strip_unwanted_chars(dates_stripped_html)

dates_formatted = datex.format_months(dates_stripped_datechars)

dates_datetime = datex.convert_to_datetime(dates_formatted)


# Show Links Section #
concert_details_html = showlinkx.scrape_concert_links(site_html, selectors["ticket_url"])


# DB Function #
utilityx.add_concert_to_database(artists_stripped, dates_datetime, concert_details_html, 5)