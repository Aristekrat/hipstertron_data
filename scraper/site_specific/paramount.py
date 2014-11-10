import sys
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx, showlinkx
import re
 
# Paramount has a bunch of special code to format it's handwritten dates.
# In retrospect, this was foolish. Paramount has a whole bunch of regularly formatted dates hidden by Javascript. 
# Pulling it from the top banner was way more work than it was worth. 
# Parmount needs to be REDONE.

urls = ["http://www.paramountdenver.com/"]

artist_selector = ".photo-meta-data h2 a"

date_selector = ".photo-meta-data p"

concert_details_selector = ".photo-meta-data h2 a"

site_html = sitex.get_pages(urls)


#Artist Section#

artists_html = artistx.scrape_artists(site_html, artist_selector)

artists_stripped = utilityx.strip_html(artists_html)


#Dates Section#

dates_html = datex.scrape_dates(site_html, date_selector)

dates_stripped_html = utilityx.strip_html(dates_html)

dates_stripped_datechars = datex.strip_unwanted_datechars(dates_stripped_html)

# This function removes any result that does not have 'day' in it, most of the non-conforming paramount results don't.
def remove_junk(results):
	stripped = []
	for date in results:
		x = re.search('day|Nov', date) #Note this condition is not foolproof. Sometimes Paramount doesn't even include the damn day.
		if (x != None):
			stripped.append(date)
	return stripped

dates_special_mod1 = remove_junk(dates_stripped_datechars)



#Show Links Section#

concert_details_html = showlinkx.scrape_concert_links(site_html, concert_details_selector)

# This function grabs reasonably consistent dates and boots out the remainder. FU paramount.
def cull_dates(results):
	stripped = []
	for index, date in enumerate(results):
		x = date.split()
		x.pop(0)
		t = x[0][:3]
		if (t == "Sep" or t == "Oct" or t == "Nov" or t == "Dec" or t == "Jan" or t == "Feb" or t == "Mar" or t == "Apr"):
			culled = " ".join(x[:2])
			stripped.append(culled)
		else: 
			artists_stripped.pop(index)
			concert_details_html.pop(index)
	return stripped

dates_special_mod2 = cull_dates(dates_special_mod1)

dates_format1 = datex.format_months(dates_special_mod2)

dates_format2 = datex.add_year(dates_format1)

dates_datetime = datex.convert_to_datetime(dates_format2)

utilityx.add_concert_to_database(artists_stripped, dates_datetime, concert_details_html, 7)