import sys
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx

# Received Error, not functional

urls = ["http://www.fillmoreauditorium.org/events/"]

artist_selector = ".eventInfo h3 a"

date_selector = ".eventInfo strong"

def fillmore_modify_string(results):
	stripped = []
	for result in results:
		result = result.split(' ')
		result.insert(-1, result[0])
		del result[0]
		stripped.append(" ".join(result))
	return stripped

site_html = sitex.get_pages(urls)

#Artist Section#

artists_html = artistx.scrape_artists(site_html, artist_selector)

artists_stripped = utilityx.strip_html(artists_html)

#Dates Section#

dates_html = datex.scrape_dates(site_html, date_selector)

dates_stripped_html = utilityx.strip_html(dates_html)

dates_stripped_datechars = datex.strip_unwanted_datechars(dates_stripped_html)

dates_stripped_ends = utilityx.strip_string_ends(dates_stripped_datechars, 0, 9)

dates_special_mod1 = fillmore_modify_string(dates_stripped_ends)

dates_datetime = datex.convert_to_datetime(dates_special_mod1)

utilityx.add_concert_to_database(artists_stripped, dates_datetime, 4)