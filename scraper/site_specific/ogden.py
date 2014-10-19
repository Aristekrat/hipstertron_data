import sys
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx, showlinkx

# Fully functional

urls = ["http://www.ogdentheatre.com/events", 
"http://www.ogdentheatre.com/events/index/20",
"http://www.ogdentheatre.com/events/index/40"]

artist_selector = ".entry h3"

date_selector = ".date"

concert_details_selector = ".entry .buttons a"

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

#Show Links Section#

concert_details_html = showlinkx.scrape_concert_links(site_html, concert_details_selector)

utilityx.add_concert_to_database(artists_stripped, dates_datetime, concert_details_html, 3)