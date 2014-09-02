import sitex
import artistx
import datex
import utilityx

#Note - the dates for Pepsi Center are inconsistent and need more work. 
# Lengths are equal

urls = ["http://www.pepsicenter.com/"]

artist_selector = ".image-title a"

date_selector = ".image-line2"

site_html = sitex.get_pages(urls)

#Artist Section#

artists_html = artistx.scrape_artists(site_html, artist_selector)

artists_stripped = utilityx.strip_html(artists_html)

#Dates Section#

dates_html = datex.scrape_dates(site_html, date_selector)

dates_stripped_html = utilityx.strip_html(dates_html)

dates_stripped_datechars = datex.strip_unwanted_datechars(dates_stripped_html)

#dates_stripped_ends = utilityx.strip_string_ends(dates_stripped_datechars, 4, 8)

#dates_datetime = datex.convert_to_datetime(dates_stripped_ends)