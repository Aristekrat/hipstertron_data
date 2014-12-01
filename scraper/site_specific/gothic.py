import sys
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx, showlinkx, site_specificx
from libraries import selector_library, urls_library

selectors = selector_library.gothic

urls = urls_library.urls["gothic"]

site_html = sitex.get_pages(urls)


#Artist Section#
artists_html = sitex.generic_scrape(site_html, selectors['artist'])

artists_stripped_html = utilityx.strip_html(artists_html)

artists_stripped = utilityx.strip_unwanted_chars(artists_stripped_html)


#Dates Section#
dates_html = sitex.generic_scrape(site_html, selectors['date'])

dates_stripped_html = site_specificx.special_strip_html(dates_html)

dates_stripped_datechars = utilityx.strip_unwanted_chars(dates_stripped_html)

dates_formatted = datex.format_months(dates_stripped_datechars)

dates_datetime = datex.convert_to_datetime(dates_formatted)


#Concert Links Section#
concert_details_html = showlinkx.scrape_concert_links(site_html, selectors['ticket_url'])


# DB Function #
utilityx.add_concert_to_database(artists_stripped, dates_datetime, concert_details_html, 1)