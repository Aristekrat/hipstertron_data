import sys
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx, showlinkx

#Red Rocks, dates are being duplicated and strangely the number matches the # of artists. 

urls = ["http://redrocksonline.com/concerts-events/calendar/2014/09",
"http://redrocksonline.com/concerts-events/calendar/2014/10"]

artist_selector = "li .concert"

#date_selector = ".date"

concert_details_selector = "li .concert"

site_html = sitex.get_pages(urls)

#Artist Section#

artists_html = artistx.scrape_artists(site_html, artist_selector)

artists_stripped = utilityx.strip_html(artists_html)

artists_special_mod1 = utilityx.strip_string_ends(artists_stripped, 0, 10)

#Dates Section#

# Special Red Rocks functions, really need to find a better way in the future
def get_redrocks_dateurls(results):
	dates = []
	for result in results: 
		for x in result:
			dates.append(x.attrs['href'])
	return dates

def scrape_redrocks_dates(pages): 
	scraped = []
	for page in pages:
		scraped.append(page.find(class_ = "date_time"))
	return scraped

def redrocks_strip_dates(results):
	i = 1
	stripped = []
	for result in results:
		if result and i % 2 == 0:
			stripped.append(result)
		i = i + 1
	return stripped

redrocks_date_urls = get_redrocks_dateurls(artists_html)

redrocks_date_pages = sitex.get_pages(redrocks_date_urls)

dates_html = scrape_redrocks_dates(redrocks_date_pages)

dates_stripped_html = utilityx.strip_html(dates_html)

dates_stripped_datechars = datex.strip_unwanted_datechars(dates_stripped_html)

dates_special_mod1 = redrocks_strip_dates(dates_stripped_datechars)

dates_datetime = datex.convert_to_datetime(dates_special_mod1)

#Show Links Section#

concert_details_html = showlinkx.scrape_concert_links(site_html, concert_details_selector)

utilityx.add_concert_to_database(artists_special_mod1, dates_datetime, concert_details_html, 9)