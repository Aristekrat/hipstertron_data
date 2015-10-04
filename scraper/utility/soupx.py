from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
#from memory_profiler import profile

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
	soup_pages = []
	# This block uses ~70MB of memory. The for loop uses no memory	
	for url in urls:
		try: 
			# ~24
			req = Request(url, headers = header)
			soupified = BeautifulSoup(urlopen(req))
			# Accumulator is ~ 43
			soup_pages.append(soupified)
		except:
			continue
	return soup_pages

# This function returns just the selected results from a full BS4 obj and converts the BS4 obj into a string
# This function is more limited than get_pages but it is also significantly more memory efficient
def get_results_from_pages(urls, selector):
	soup_strings = []
	for url in urls:
		try: 
			req = Request(url, headers = header)
			soup_strings.append(str(BeautifulSoup(urlopen(req)).select(selector)))
		except:
			continue
	return soup_strings


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

