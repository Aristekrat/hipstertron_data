from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from time import strptime

#Venue List: Bluebird Theatre, Fox Theatre, Fillmore Auditoriom, First Bank Center, Pepsi Center, Red Rocks Ampitheatre, Gothic Theatre
#Add Now: http://www.ogdentheatre.com/events/, http://www.fiddlersgreenamp.com/events
#Add in the Future: Summit Music Hall, Cervantes Masterpiece, Swallow Hill Music, Boetttcher Concert Hall, Larimer Lounge, Hi-Dive

#Scraping data 
bluebird_urls = ["http://www.bluebirdtheater.net/events", 
"http://www.bluebirdtheater.net/events/index/10", 
"http://www.bluebirdtheater.net/events/index/20",
"http://www.bluebirdtheater.net/events/index/30",
"http://www.bluebirdtheater.net/events/index/40",
"http://www.bluebirdtheater.net/events/index/50",
"http://www.bluebirdtheater.net/events/index/60"]

paramount_urls = ["http://www.paramountdenver.com/"]

foxtheatre_urls = ["http://www.foxtheatre.com/"]

fillmore_urls = ["http://www.fillmoreauditorium.org/events/"]

firstbank_urls = ["http://www.1stbankcenter.com/events", "http://www.1stbankcenter.com/events/index/10"]

pepsi_urls = ["http://www.pepsicenter.com/"]

redrocks_urls = ["http://redrocksonline.com/concerts-events/calendar", 
"http://redrocksonline.com/concerts-events/calendar/2014/09",
"http://redrocksonline.com/concerts-events/calendar/2014/10"]

gothic_urls = ["http://www.gothictheatre.com/events", 
"http://www.gothictheatre.com/events/index/10",
"http://www.gothictheatre.com/events/index/20",
"http://www.gothictheatre.com/events/index/30",
"http://www.gothictheatre.com/events/index/40"]

bluebird_artist_selector = ".info h3 a"
paramount_artist_selector = ".photo-meta-data h2 a"
fillmore_artist_selector = ".eventInfo h3 a"
pepsicenter_artist_selector = ".image-title a"
firstbank_artist_selector = ".info h3 a"
redrocks_artist_selector = "li .concert"
gothic_artist_selector = ".entry h3"

bluebird_date_selector = ".date"
paramount_date_selector = ".photo-meta-data p"
fillmore_date_selector = ".eventInfo strong"
pepsicenter_date_selector = ".image-line2"
firstbank_date_selector = ".date"
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

def fillmore_modify_string(results):
	stripped = []
	for result in results:
		result = result.split(' ')
		result.insert(-1, result[0])
		del result[0]
		stripped.append(" ".join(result))
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

# Get Urls and convert to soup object
def get_pages(urls):
	soup_page = []
	for url in urls:
		req = Request(url, headers = header)
		page = urlopen(req)
		soupified = BeautifulSoup(page)
		soup_page.append(soupified)
	return soup_page

bluebird = get_pages(bluebird_urls)
paramount = get_pages(paramount_urls)
fillmore = get_pages(fillmore_urls)
pepsicenter = get_pages(pepsi_urls)
firstbank = get_pages(firstbank_urls)
redrocks = get_pages(redrocks_urls)
gothic = get_pages(gothic_urls)

# Artist scraping section
def scrape_artists(pages, selector):
	scraped = []
	for page in pages:
		scraped.append(page.select(selector))
	return scraped

bluebird_artists = scrape_artists(bluebird, bluebird_artist_selector)
paramount_artists = scrape_artists(paramount, paramount_artist_selector)
fillmore_artists = scrape_artists(fillmore, fillmore_artist_selector)
pepsicenter_artists = scrape_artists(pepsicenter, pepsicenter_artist_selector)
firstbank_artists = scrape_artists(firstbank, firstbank_artist_selector)
redrocks_artists_raw = scrape_artists(redrocks, redrocks_artist_selector)
gothic_artists = scrape_artists(gothic, gothic_artist_selector)

bluebird_artists = strip_html(bluebird_artists)
paramount_artists = strip_html(paramount_artists)
fillmore_artists = strip_html(fillmore_artists)
pepsicenter_artists = strip_html(pepsicenter_artists)
firstbank_artists = strip_html(firstbank_artists)
redrocks_artists = strip_html(redrocks_artists_raw)
gothic_artists = strip_html(gothic_artists)

redrocks_artists = strip_string_ends(redrocks_artists, 0, 10)

# Dates scraping section

def scrape_dates(pages, selector):
	scraped = []
	for page in pages:
		date = page.select(selector)
		scraped.append(date)
	return scraped

bluebird_dates = scrape_dates(bluebird, bluebird_date_selector)
paramount_dates = scrape_dates(paramount, paramount_date_selector)
fillmore_dates = scrape_dates(fillmore, fillmore_date_selector)
pepsicenter_dates = scrape_dates(pepsicenter, pepsicenter_date_selector)
firstbank_dates = scrape_dates(firstbank, firstbank_date_selector)
gothic_dates = scrape_dates(gothic, gothic_date_selector)

# Special Red Rocks section, look to harmonize in the future
#Red Rocks
def get_redrocks_dateurls(results):
	dates = []
	for result in results: 
		for x in result:
			dates.append(x.attrs['href'])
	return dates

redrocks_date_urls = get_redrocks_dateurls(redrocks_artists_raw)

def get_redrocks_dates(urls):
	date_pages = []
	for url in urls:
		page = urlopen(url)
		x = BeautifulSoup(page)
		date_pages.append(x)
	return date_pages

redrocks_date_pages = get_redrocks_dates(redrocks_date_urls)

def scrape_redrocks_dates(pages): 
	scraped = []
	for page in pages:
		scraped.append(page.find(class_ = "date_time"))
	return scraped

redrocks_dates = scrape_redrocks_dates(redrocks_date_pages)
# Back to overall section
bluebird_dates = strip_html(bluebird_dates)
paramount_dates = strip_html(paramount_dates)
fillmore_dates = strip_html(fillmore_dates)
pepsicenter_dates = strip_html(pepsicenter_dates)
firstbank_dates = strip_html(firstbank_dates)
redrocks_dates = strip_html(redrocks_dates)
gothic_dates = strip_html(gothic_dates)

def strip_unwanted_datechars(results):
	remap = {
		ord('\n') : None,
		ord('\t') : None,
		ord(',') : None
	}
	stripped = []
	for result in results:
		stripped.append(result.translate(remap))
	return stripped

def paramount_strip_dates(results):
	stripped = []
	for result in results:
		if (result.find("now") == -1):
			stripped.append(result)
	return stripped

def redrocks_strip_dates(results):
	i = 1
	stripped = []
	for result in results:
		if result and i % 2 == 0:
			stripped.append(result)
		i = i + 1
	return stripped

bluebird_dates = strip_unwanted_datechars(bluebird_dates)
paramount_dates = paramount_strip_dates(paramount_dates)
firstbank_dates = strip_unwanted_datechars(firstbank_dates)
redrocks_dates = strip_unwanted_datechars(redrocks_dates)
gothic_dates = strip_unwanted_datechars(gothic_dates)
redrocks_dates = redrocks_strip_dates(redrocks_dates)

bluebird_dates = strip_string_ends(bluebird_dates, 4, 8)
firstbank_dates = strip_string_ends(firstbank_dates, 4, 8)
fillmore_dates = strip_string_ends(fillmore_dates, 0, 9)
gothic_dates = strip_string_ends(gothic_dates, 4, 8)
fillmore_dates = fillmore_modify_string(fillmore_dates)

def convert_to_datetime(results):
	converted = []
	for result in results:
		x = strptime(result, "%B %d %Y")
		converted.append(x)
	return converted

#bluebird_dates = convert_to_datetime(bluebird_dates) #Has strange non-spaces in the 2nd and 3rd results that throw off this function.
#paramount_dates = convert_to_datetime(paramount_dates) #Very inconsistent
fillmore_dates = convert_to_datetime(fillmore_dates)
firstbank_dates = convert_to_datetime(firstbank_dates)
gothic_dates = convert_to_datetime(gothic_dates)
redrocks_dates = convert_to_datetime(redrocks_dates)
#print(pepsicenter_dates) #Inconsistent