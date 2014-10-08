import sys
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx

# Fully functional

urls = ["http://www.bluebirdtheater.net/events", 
"http://www.bluebirdtheater.net/events/index/10", 
"http://www.bluebirdtheater.net/events/index/20",
"http://www.bluebirdtheater.net/events/index/30",
"http://www.bluebirdtheater.net/events/index/40",
"http://www.bluebirdtheater.net/events/index/50",
"http://www.bluebirdtheater.net/events/index/60"]

artist_selector = ".info h3 a"

date_selector = ".date"

site_html = sitex.get_pages(urls)

#Artist Section#

artists_html = artistx.scrape_artists(site_html, artist_selector)

artists_stripped = utilityx.strip_html(artists_html)

#Dates Section#

dates_html = datex.scrape_dates(site_html, date_selector)

dates_stripped_html = utilityx.strip_html(dates_html)

dates_stripped_datechars = datex.strip_unwanted_datechars(dates_stripped_html)

dates_stripped_ends = utilityx.strip_string_ends(dates_stripped_datechars, 4, 8)

dates_datetime = datex.convert_to_datetime(dates_stripped_ends)

utilityx.add_concert_to_database(artists_stripped, dates_datetime, 2)