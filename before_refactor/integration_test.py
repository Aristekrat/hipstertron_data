from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from time import strptime

#This file tests whether it is possible to save the scraping results in database and then later retrieve them. 

gothic_urls = ["http://www.gothictheatre.com/events", 
"http://www.gothictheatre.com/events/index/10",
"http://www.gothictheatre.com/events/index/20",
"http://www.gothictheatre.com/events/index/30",
"http://www.gothictheatre.com/events/index/40"]

gothic_artist_selector = ".entry h3"

gothic_date_selector = ".date"

# Scraping Utility 

#Works for dates and artists
def strip_html(results):
	stripped = []
	for result in results:
		for x in result:
			stripped.append(x.string)
	return stripped

def strip_string_ends(results, beginning, end):
	stripped = []
	for result in results: 
		stripped.append(result[beginning:-end])
	return stripped

# Dummy header for the get pages function. 
header = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.8",
	"Cache-Control": "no-cache",
	"Connection": "keep-alive",
	"Referer": "https://www.google.com/"
}

x = []
# Get Urls and convert to soup object
def get_pages(urls):
	soup_page = []
	for url in urls:
		req = Request(url, headers = header)
		page = urlopen(req)
		x.append(page)
		soupified = BeautifulSoup(page)
		soup_page.append(soupified)
	return soup_page

gothic = get_pages(gothic_urls)

#print(gothic)
print(x)