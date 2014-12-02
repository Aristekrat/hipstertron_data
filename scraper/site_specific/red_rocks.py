import sys
sys.path.append("..")
from utility import sitex, datex, utilityx, showlinkx, site_specificx
from libraries import selector_library, urls_library

selectors = selector_library.red_rocks

urls = urls_library.urls["red_rocks"]

site_html = sitex.get_pages(urls)


# Artist Section #
artists_html = sitex.generic_scrape(site_html, selectors["artist"])

artists_stripped = utilityx.strip_html(artists_html)

artists_special_mod1 = utilityx.strip_string_ends(artists_stripped, 0, 10)


# Dates Section #
redrocks_date_urls = site_specificx.get_redrocks_dateurls(artists_html)

redrocks_date_pages = sitex.get_pages(redrocks_date_urls)

dates_html = site_specificx.scrape_redrocks_dates(redrocks_date_pages)

dates_stripped_html = utilityx.strip_html(dates_html)

dates_stripped_datechars = utilityx.strip_unwanted_chars(dates_stripped_html)

dates_special_mod1 = site_specificx.redrocks_strip_dates(dates_stripped_datechars)

dates_datetime = datex.convert_to_datetime(dates_special_mod1)


# Show Links Section #
concert_details_html = showlinkx.scrape_concert_links(site_html, selectors["ticket_url"])


# DB Function #
utilityx.add_concert_to_database(artists_special_mod1, dates_datetime, concert_details_html, 9)