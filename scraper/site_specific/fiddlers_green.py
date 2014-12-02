import sys
sys.path.append("..")
from utility import sitex, datex, utilityx

#Note, currently aren't any shows listed so fiddler's should properly be returning 0 results. 

urls = ["http://www.fiddlersgreenamp.com/events"]

artist_selector = ".entry h3"

date_selector = ".date"

site_html = sitex.get_pages(urls)

#Artist Section#

artists_html = artistx.scrape_artists(site_html, artist_selector)

artists_stripped = utilityx.strip_html(artists_html)

#Dates Section#

dates_html = datex.scrape_dates(site_html, date_selector)

dates_stripped_html = utilityx.strip_html(dates_html)

dates_stripped_datechars = utilityx.strip_unwanted_chars(dates_stripped_html)

dates_stripped_ends = utilityx.strip_string_ends(dates_stripped_datechars, 4, 8)

dates_datetime = datex.convert_to_datetime(dates_stripped_ends)

utilityx.add_concert_to_database(artists_stripped, dates_datetime, 6)