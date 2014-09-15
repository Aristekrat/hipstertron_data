import sitex
import artistx
import datex
import utilityx
import re

#Note - the dates for Pepsi Center are inconsistent and need more work. 
# Lengths are equal

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

#Cleans up the pepsi dates successfully but way inefficent. Come back to this once you learn more about regex.
def pepsi_get_dates(results):
	stripped = []
	for date in results:
		x = re.search('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec', date)
		t = re.search('^Date', date)
		if (x != None and t == None):
			stripped.append(date)
	return stripped

dates_html = datex.scrape_dates(site_html, date_selector)
alt_dates_html = datex.scrape_dates(site_html, date_selector)

dates_stripped_html = utilityx.strip_html(dates_html)
alt_dates_stripped_html = utilityx.strip_html(alt_dates_html)

dates_stripped_datechars = datex.strip_unwanted_datechars(dates_stripped_html)
alt_dates_stripped_datechars = datex.strip_unwanted_datechars(alt_dates_stripped_html)

merged_dates = dates_stripped_datechars + alt_dates_stripped_datechars

#Still need to strip the day (eg, Thursday, Monday, etc), the time, and add the year.
pepsi_dates = pepsi_get_dates(merged_dates)