import sys
sys.path.append("..")
from utility import sitex, datex, utilityx, showlinkx, site_specificx
from libraries import selector_library, urls_library

selectors = selector_library.paramount

urls = urls_library.urls["paramount"]

site_html = sitex.get_pages(urls)


#Artist Section#
artists_html = sitex.generic_scrape(site_html, selectors["artist"])

artists_stripped = utilityx.strip_html(artists_html)


#Dates Section#
dates_html = sitex.generic_scrape(site_html, selectors["date"])

dates_stripped_html = datex.cull_date_and_month(dates_html[0]) #Not quite sure why paramount is pulling down something different

dates_stripped_datechars = utilityx.strip_unwanted_chars(dates_stripped_html)

dates_formatted = datex.add_year(dates_stripped_datechars)

dates_datetime = datex.convert_to_datetime(dates_formatted)


#Show Links Section#
concert_details_html = showlinkx.scrape_concert_links(site_html, selectors["ticket_url"])


# DB Function #
utilityx.add_concert_to_database(artists_stripped, dates_datetime, concert_details_html, 7)

print("End of Paramount script reached, exiting.")