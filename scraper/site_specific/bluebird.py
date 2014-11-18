import sys
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx, showlinkx

# Selector library #
artist_selector = ".entry h3 a"

date_selector = ".date"

url_selector = ".final .number"

concert_details_selector = ".entry .buttons a"


# URL Harvest #
root_url = ["http://www.bluebirdtheater.net/events"]

root = sitex.get_pages(root_url)

urls = showlinkx.scrape_concert_pages(root, root_url, url_selector)

site_html = sitex.get_pages(urls)


# Artist Section #
artists_html = artistx.scrape_artists(site_html, artist_selector)

artists_stripped_html = utilityx.strip_html(artists_html)

artists_stripped = utilityx.strip_unwanted_chars(artists_stripped_html)


# Dates Section #
dates_html = datex.scrape_dates(site_html, date_selector)

# The site maintainers added an internal span which messed with BeautifulSoup's ability to access obj.string, which necessitated this site specific function
def special_strip_html(results):
	stripped = []
	for result in results:
		for x in result:
			z = str(x)
			t = z.split()
			stripped_date = " ".join(t[6:9])
			stripped.append(stripped_date)
	return stripped

dates_stripped_html = special_strip_html(dates_html)

dates_stripped_datechars = utilityx.strip_unwanted_chars(dates_stripped_html)

dates_formatted = datex.format_months(dates_stripped_datechars)

dates_datetime = datex.convert_to_datetime(dates_formatted)


# Show Links Section #
concert_details_html = showlinkx.scrape_concert_links(site_html, concert_details_selector)


# DB Add function #
utilityx.add_concert_to_database(artists_stripped, dates_datetime, concert_details_html, 2)