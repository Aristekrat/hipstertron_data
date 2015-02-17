from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

header = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.8",
	"Cache-Control": "no-cache",
	"Connection": "keep-alive",
	"Referer": "https://www.google.com/"
}

def strip_html(results):
	stripped = []
	for result in results:
		for x in result:
			stripped.append(x.string)
	return stripped

# Get Urls and convert to soup object. Works on many or one url
def get_pages(urls):
	soup_page = []
	for url in urls:
		try: 
			req = Request(url, headers = header)
			page = urlopen(req)
			soupified = BeautifulSoup(page)
			soup_page.append(soupified)
		except:
			continue
	return soup_page

# The standard function for both artist and date scraping
def generic_scrape(pages, selector):
	scraped = []
	for page in pages:
		scraped.append(page.select(selector))
	return scraped

# This function is almost a mirror image of generic scrape, yet using generic scrape in its place will cause Red Rocks to find a list of None results.
# page.find and page.select must work differently. It bears investigating
def scrape_by_class(pages, selector): 
	scraped = []
	for page in pages:
		scraped.append(page.find(class_ = selector))
	return scraped

