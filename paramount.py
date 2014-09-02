import sitex
import artistx
import datex
import utilityx

#Note: Paramount's Dates are highly inconsistent, needs more work
# Lengths are not equal, artists was shorter than dates.

urls = ["http://www.paramountdenver.com/"]

artist_selector = ".photo-meta-data h2 a"

date_selector = ".photo-meta-data p"

def paramount_strip_dates(results):
	stripped = []
	for result in results:
		if (result.find("now") == -1):
			stripped.append(result)
	return stripped

site_html = sitex.get_pages(urls)

#Artist Section#

artists_html = artistx.scrape_artists(site_html, artist_selector)

artists_stripped = utilityx.strip_html(artists_html)

#Dates Section#

dates_html = datex.scrape_dates(site_html, date_selector)

dates_stripped_html = utilityx.strip_html(dates_html)

dates_stripped_datechars = datex.strip_unwanted_datechars(dates_stripped_html)

#dates_stripped_ends = utilityx.strip_string_ends(dates_stripped_datechars, 4, 8)

dates_special_mod1 = paramount_strip_dates(dates_stripped_datechars)

#dates_datetime = datex.convert_to_datetime(dates_stripped_ends)