import sys
sys.path.append("../../scraper")
sys.path.append("../..")
from utility import sitex, datex, utilityx, showlinkx, site_specificx 
from libraries import urls_library, selector_library

target = sys.argv[1]

root_url = urls_library.urls[target]

# selectors = selector_library.fillmore

# # URL Harvest #
# root = sitex.get_pages(root_url)

# urls = site_specificx.scrape_concert_pages(root, root_url, selectors["page_url"])

site_html = sitex.get_pages(root_url)

write_file = target + ".html"

fillmore_source = open(write_file, 'w')

fillmore_source.write(str(site_html[0]))

fillmore_source.close()