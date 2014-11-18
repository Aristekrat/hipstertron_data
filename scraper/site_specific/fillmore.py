import sys
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx, showlinkx

#Selector Library 
url_selector = "a.page-numbers"

artist_selector = ".eventInfo h3 a"

date_selector = ".eventInfo strong"

concert_details_selector = ".buyNowTicket a"


# URL Harvest #
root_url = ["http://www.fillmoreauditorium.org/events/"]

root = sitex.get_pages(root_url)

#The fillmore has relative links and it currently doesn't have a unique css selector for pages
#Thus, a site specific function is required
def scrape_concert_pages(root_page, root_url, selector):
	scraped = [root_url[0]]
	x = root_page[0].select(selector)
	for r in x:
		if r.string != ">":
			scraped.append("http://www.fillmoreauditorium.org" + r.attrs['href'])
	return scraped

urls = scrape_concert_pages(root, root_url, url_selector)

site_html = sitex.get_pages(urls)


# Artist Section #
artists_html = artistx.scrape_artists(site_html, artist_selector)

artists_stripped = utilityx.strip_html(artists_html)


# Dates Section #
# Why is this thing necessary? 
def fillmore_modify_string(results):
	stripped = []
	for result in results:
		result = result.split(' ')
		result.insert(-1, result[0])
		del result[0]
		stripped.append(" ".join(result))
	return stripped

dates_html = datex.scrape_dates(site_html, date_selector)

dates_stripped_html = utilityx.strip_html(dates_html)

dates_stripped_datechars = utilityx.strip_unwanted_chars(dates_stripped_html)

dates_stripped_ends = utilityx.strip_string_ends(dates_stripped_datechars, 0, 9)

dates_special_mod1 = fillmore_modify_string(dates_stripped_ends)

dates_datetime = datex.convert_to_datetime(dates_special_mod1)


# Show Links Section #
concert_details_html = showlinkx.scrape_concert_links(site_html, concert_details_selector)


# DB Function #
utilityx.add_concert_to_database(artists_stripped, dates_datetime, concert_details_html, 4)