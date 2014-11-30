import re
import sys
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx, showlinkx, site_specificx, selector_library, urls_library

urls = urls_library.urls["pepsi_center"]

selectors = selector_library.pepsi_center

site_html = sitex.get_pages(urls)


# Artist Section #
artists_html = artistx.scrape_artists(site_html, selectors["artist"])

artists_stripped = utilityx.strip_html(artists_html)

artists_special_mod1 = site_specificx.pepsi_strip_artists(artists_stripped)


# Dates Section #
# TODO - create a utility function that finds dates by regex and use it here
dates_html = datex.scrape_dates(site_html, selectors["date"])

dates_stripped_html = utilityx.strip_html(dates_html)

dates_special_mod1 = site_specificx.get_proper_dates(dates_stripped_html, artists_special_mod1)

dates_special_mod2 = datex.cull_date_and_month(dates_special_mod1)

dates_format1 = utilityx.strip_unwanted_chars(dates_special_mod2)

dates_format2 = datex.format_months(dates_special_mod2)

dates_format3 = datex.add_year(dates_format1)

dates_datetime = datex.convert_to_datetime(dates_format3)


# Show Links Section #
concert_details_html = showlinkx.scrape_concert_links(site_html, selectors["ticket_url"])

# Taylor Swift's announced concert doesn't have a buy tickets link, which messes up the add to db function. 
# This is a bandaid to deal with it. I generally assume this won't be a common problem. 
concert_details_html.append("/")

# DB Function #
utilityx.add_concert_to_database(artists_special_mod1, dates_datetime, concert_details_html, 8)