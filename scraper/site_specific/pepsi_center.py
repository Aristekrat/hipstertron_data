import sys
sys.path.append("..")
from utility import sitex, datex, utilityx, showlinkx, site_specificx
from libraries import selector_library, urls_library

urls = urls_library.urls["pepsi_center"]

selectors = selector_library.pepsi_center

site_html = sitex.get_pages(urls)


# Artist Section #
artists_html = sitex.generic_scrape(site_html, selectors["artist"])

artists_stripped = utilityx.strip_html(artists_html)

artists_special_mod1 = site_specificx.pepsi_strip_artists(artists_stripped)


# Dates Section #
dates_html = sitex.generic_scrape(site_html, selectors["date"])

dates_stripped_html = utilityx.strip_html(dates_html)

# TODO - create a utility function that finds dates by regex and use it here
dates_special_mod1 = utilityx.remove_listings_without_dates(dates_stripped_html, artists_special_mod1)

dates_culled = datex.cull_date_and_month(dates_special_mod1)

dates_stripped_datechars = utilityx.strip_unwanted_chars(dates_culled)

dates_formatted = datex.add_year(dates_format1)

dates_datetime = datex.convert_to_datetime(dates_formatted)


# Show Links Section #
concert_details_html = showlinkx.scrape_concert_links(site_html, selectors["ticket_url"])

# Taylor Swift's announced concert doesn't have a buy tickets link, which messes up the add to db function. 
# This is a bandaid to deal with it. I generally assume this won't be a common problem. 
# TODO - gotta fix this
concert_details_html.append("/")

# DB Function #
utilityx.add_concert_to_database(artists_special_mod1, dates_datetime, concert_details_html, 8)

print("End of Pepsi Center script reached, exiting.")