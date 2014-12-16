import sys
sys.path.append("../../scraper")
sys.path.append("../..")
from utility import soupx 
from libraries import urls_library

target = sys.argv[1]

root_url = urls_library.urls[target]

site_html = soupx.get_pages(root_url)

write_file = target + ".html"

source = open(write_file, 'w')

source.write(str(site_html[0]))

source.close()