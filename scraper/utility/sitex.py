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

# Get Urls and convert to soup object
def get_pages(urls):
	soup_page = []
	for url in urls:
		req = Request(url, headers = header)
		page = urlopen(req)
		soupified = BeautifulSoup(page)
		soup_page.append(soupified)
	return soup_page

# Scrapes pretty much any data type
def selenium_scrape(selector, driver):
	stripped = []
	t = driver.find_elements_by_css_selector(selector)
	for result in t:
		stripped.append(result.get_attribute('innerHTML'))
	return stripped
