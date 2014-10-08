import sys
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx
import re

#Note - Date Problems: cannot handle the cavalia entry, it harvest both dates as seperate entries rather than using them as a range.
# Is not properly harvesting the Katy Perry Sept. 30th date. 

urls = ["http://www.pepsicenter.com/"]

artist_selector = ".image-title a"

date_selector = ".image-line2"
alt_date_selector = ".image-line3"

site_html = sitex.get_pages(urls)

#Artist Section#

def pepsi_strip_artists(results):
	stripped = []
	for artist in results:
		x = re.split('[:"-]', artist)
		stripped.append(str(x[0]))
	return stripped

artists_html = artistx.scrape_artists(site_html, artist_selector)

artists_stripped = utilityx.strip_html(artists_html)

artists_special_mod1 = pepsi_strip_artists(artists_stripped)

#Dates Section

# I use the double dates because the selector that the date is on varies. Need to come up with a better method. 
dates_html = datex.scrape_dates(site_html, date_selector)
alt_dates_html = datex.scrape_dates(site_html, alt_date_selector)

dates_stripped_html = utilityx.strip_html(dates_html)
alt_dates_stripped_html = utilityx.strip_html(alt_dates_html)

dates_stripped_datechars = datex.strip_unwanted_datechars(dates_stripped_html)
alt_dates_stripped_datechars = datex.strip_unwanted_datechars(alt_dates_stripped_html)

# Search for proper date, if none found search backup, if not found there delete. 
def get_proper_dates(results, alt_results):
	stripped = []
	for index, date in enumerate(results): 
		x = re.search('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec', date)
		if (x == None):
			t = re.search('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec', alt_results[index])
			if (t == None):
				artists_special_mod1.pop(index)
				continue
			else:
				x = t
		stripped.append(x.string)
	return stripped

dates_special_mod1 = get_proper_dates(dates_stripped_datechars, alt_dates_stripped_datechars)

#Harvests the date from the string
def cull_dates(results):
	culled = []
	for date in results:
		components = date.split()
		for index, component in enumerate(components): 
			x = re.search('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec', component)
			if (x == None):
				continue
			elif (x != None):
				culled.append(components[index] + " " + components[index + 1])
				break
	return culled

dates_special_mod2 = cull_dates(dates_special_mod1)

dates_format1 = datex.format_months(dates_special_mod2)

dates_format2 = datex.add_year(dates_format1)

dates_datetime = datex.convert_to_datetime(dates_format2)

utilityx.add_concert_to_database(artists_special_mod1, dates_datetime, 8)