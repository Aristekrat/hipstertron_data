from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import sqlite3

#Venue List: Fillmore Auditorium - Optional: Summit Music Hall, Cervantes Masterpiece, Swallow Hill Music, Boetttcher Concert Hall, Larimer Lounge, Hi-Dive

#Fillmore Auditorium
# http://www.fillmoreauditorium.org/events/
# .eventInfo strong / eventInfo a title attribute

def get_page():
	url = "http://www.fillmoreauditorium.org/events/"
	page = urlopen(url)
	soup_page = BeautifulSoup(page)
	return soup_page

fillmore = get_page()

def scrape_dates(page):
	scraped = page.select(".eventInfo strong")
	return scraped

dates = scrape_dates(fillmore)

def strip_html(results):
	stripped = []
	for result in results:
		stripped.append(result.string)

	return stripped

dates = strip_html(dates)

'''
# Fox Theatre
# The information I need is contained in a big javascript variable. 
def get_page():
	soup_page = []
	url = ("http://www.foxtheatre.com/")
	page = urlopen(url)
	soup_page = BeautifulSoup(page)
	return soup_page

fox = get_page()

def scrape_artists(page):
	scraped = []
	for result in page:
		scraped.append(page.select("img"))
	return scraped

artists = scrape_artists(fox)

def remove_unwanted_chars(results):
	scraped = []
	for result in results:
		scraped.append(result.attrs['alt'])
	return scraped
'''

'''
def get_date_urls(results):
	dates = []
	for result in results: 
		for x in result:
			dates.append(x.attrs['href'])
	return dates

date_urls = get_date_urls(raw_results)
'''

''' Mostly works, although date is returning a bunch of unwanted : 'Tickets on-sale now!'
# Paramount Theatre

def get_page():
	url = "http://www.paramountdenver.com/"
	page = urlopen(url)
	soup_page = BeautifulSoup(page)
	return soup_page

paramountdenver = get_page()

def scrape_artists(page):
	scraped = page.select(".photo-meta-data h2 a")
	return scraped

artists = scrape_artists(paramountdenver)

def scrape_dates(page):
	scraped = page.select(".photo-meta-data p")
	return scraped

dates = scrape_dates(paramountdenver)

def strip_html(results):
	stripped = []
	for result in results:
		stripped.append(result.string)

	return stripped

dates = strip_unwanted_chars(dates)
dates = strip_html(dates)

print(dates)

artists = strip_html(artists)

'''

'''
#Pepsi Center
#Works for the Pepsi Center, although the dates need a little work
def get_pages():
	url = "http://www.pepsicenter.com/"
	page = urlopen(url)
	soup_page = BeautifulSoup(page)
	return soup_page

pepsicenter = get_pages()

def scrape_artists(page):
	scraped = page.select(".image-title a")
	return scraped

artists = scrape_artists(pepsicenter)

def scrape_dates(page):
	scraped = page.select(".image-line2")
	return scraped

dates = scrape_dates(pepsicenter)

def strip_html(results):
	stripped = []
	for result in results:
		stripped.append(result.string)

	return stripped

artists = strip_html(artists)
dates = strip_html(dates)
'''

'''
# Bluebird - Working, almost exactly the same as 1st Bank / Gothic
# http://www.bluebirdtheater.net/events, http://www.bluebirdtheater.net/events/index/10, http://www.bluebirdtheater.net/events/index/20, http://www.bluebirdtheater.net/events/index/30, http://www.bluebirdtheater.net/events/index/40 http://www.bluebirdtheater.net/events/index/50 http://www.bluebirdtheater.net/events/index/60
# .info h3 a / .date, exact same as 1st Bank

def get_pages():
	soup_page = []
	for fragment in ('', '/index/10', '/index/20', '/index/30', '/index/40', '/index/50', '/index/60'):
		url = ("http://www.bluebirdtheater.net/events" + fragment)
		page = urlopen(url)
		x = BeautifulSoup(page)
		soup_page.append(x)
	return soup_page

bluebird = get_pages()

def scrape_date(pages):
	scraped = []
	for page in pages:
		x = page.find_all(class_ = "date")
		scraped.append(x)
	return scraped

dates = scrape_date(bluebird)

def scrape_artists(pages):
	scraped = []
	for page in pages: 
		# select functionality apparently allows me to search by CSS selector
		scraped.append(page.select(".info h3 a"))
	return scraped

artists = scrape_artists(bluebird)

def strip_html(results):
	stripped = []
	for result in results:
		for x in result:
			stripped.append(x.string)

	return stripped

dates = strip_html(dates)
artists = strip_html(artists)

remap = {
	ord('\n') : None,
	ord('\t') : None
}

def strip_unwanted_chars(results):
	stripped = []
	for result in results: 
		stripped.append(result.translate(remap))
	return stripped

dates = strip_unwanted_chars(dates)

print(dates)
print(artists)

'''

''' - Working for First Bank Center - almost exactly the same as the Gothic
#1st Bank Center
#urls: http://www.1stbankcenter.com/events http://www.1stbankcenter.com/events/index/10
# .info h3 a, .date

def get_pages():
	soup_page = []
	for fragment in ('', '/index/10'):
		url = ("http://www.1stbankcenter.com/events" + fragment)
		page = urlopen(url)
		x = BeautifulSoup(page)
		soup_page.append(x)
	return soup_page

first_bank = get_pages()

def scrape_date(pages):
	scraped = []
	for page in pages:
		x = page.find_all(class_ = "date")
		scraped.append(x)
	return scraped

dates = scrape_date(first_bank)

def scrape_artists(pages):
	scraped = []
	for page in pages: 
		# select functionality apparently allows me to search by CSS selector
		scraped.append(page.select(".info h3 a"))
	return scraped

artists = scrape_artists(first_bank)

def strip_html(results):
	stripped = []
	for result in results:
		for x in result:
			stripped.append(x.string)

	return stripped

dates = strip_html(dates)
artists = strip_html(artists)

remap = {
	ord('\n') : None,
	ord('\t') : None
}

def strip_unwanted_chars(results):
	stripped = []
	for result in results: 
		stripped.append(result.translate(remap))
	return stripped

dates = strip_unwanted_chars(dates)

print(dates)
print(artists)
'''

'''
# Works for the Gothic Theatre
soup_page = []
for fragment in ('', '/index/10', '/index/20', '/index/30', '/index/40'):
	url = ("http://www.gothictheatre.com/events" + fragment)
	page = urlopen(url)
	x = BeautifulSoup(page)
	soup_page.append(x)


def scrape_date(pages):
	scraped = []
	for page in pages:
		x = page.find_all(class_ = "date")
		scraped.append(x)
	return scraped

dates = scrape_date(soup_page)

def scrape_artists(pages):
	scraped = []
	for page in pages: 
		# select functionality apparently allows me to search by CSS selector
		scraped.append(page.select(".entry h3"))
	return scraped

artists = scrape_artists(soup_page)

def strip_html(results):
	stripped = []
	for result in results:
		for x in result:
			stripped.append(x.string)

	return stripped

dates = strip_html(dates)
artists = strip_html(artists)

remap = {
	ord('\n') : None,
	ord('\t') : None
}

def strip_unwanted_chars(results):
	stripped = []
	for result in results: 
		stripped.append(result.translate(remap))
	return stripped

dates = strip_unwanted_chars(dates)

'''

''' Good for the Gothic Theatre
#conn = sqlite3.connect("hipstertron.db")

soup_page = []
for fragment in ('', '/index/10', '/index/20', '/index/30', '/index/40'):
	url = ("http://www.gothictheatre.com/events" + fragment)
	page = urlopen(url)
	x = BeautifulSoup(page)
	soup_page.append(x)


def scrape_date(pages):
	scraped = []
	for page in pages:
		x = page.find_all(class_ = "date")
		scraped.append(x)
	return scraped

dates = scrape_date(soup_page)

def scrape_artists(pages):
	scraped = []
	for page in pages: 
		# select functionality apparently allows me to search by CSS selector
		scraped.append(page.select(".entry h3"))
	return scraped

artists = scrape_artists(soup_page)

def strip_html(results):
	stripped = []
	for result in results:
		for x in result:
			stripped.append(x.string)

	return stripped

dates = strip_html(dates)
artists = strip_html(artists)

remap = {
	ord('\n') : None,
	ord('\t') : None
}

def strip_unwanted_chars(results):
	stripped = []
	for result in results: 
		stripped.append(result.translate(remap))
	return stripped

dates = strip_unwanted_chars(dates)

#print (dates)

#print(artists)

'''

'''
#Red Rocks
#urls: http://redrocksonline.com/concerts-events/calendar       http://redrocksonline.com/concerts-events/calendar/2014/09         http://redrocksonline.com/concerts-events/calendar/2014/10
# class 'concert' - date at the end of the href. Need to strip off - 8:00PM time from the concert listing.
#Mostly works for Red Rocks. Still need to polish the date functions
soup_page = []
for fragment in ('', '/2014/09', '/2014/10'):
	url = ("http://redrocksonline.com/concerts-events/calendar" + fragment)
	page = urlopen(url)
	x = BeautifulSoup(page)
	soup_page.append(x)

def scrape_artists(pages):
	scraped = []
	for page in pages: 
		scraped.append(page.select("li .concert"))
	return scraped

raw_results = scrape_artists(soup_page)

def strip_html(results):
	stripped = []
	for result in results:
		for x in result:
			stripped.append(x.string)

	return stripped

artists = strip_html(raw_results)

def strip_unwanted_chars(results):
	stripped = []
	for result in results: 
		stripped.append(result[:-10])
	return stripped

artists = strip_unwanted_chars(artists)

def get_date_urls(results):
	dates = []
	for result in results: 
		for x in result:
			dates.append(x.attrs['href'])
	return dates

date_urls = get_date_urls(raw_results)

def get_dates(urls):
	date_pages = []
	for url in urls:
		page = urlopen(url)
		x = BeautifulSoup(page)
		date_pages.append(x)
	return date_pages

date_pages = get_dates(date_urls)

def scrape_dates(pages): 
	scraped = []
	for page in pages:
		scraped.append(page.select(".date_time"))
	return scraped

dates = scrape_dates(date_pages)

print(dates)

'''

''' Error: TypeError: sequence item 0: expected bytes, bytearray, or an object with the buffer interface, dict found
headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding": "gzip,deflate,sdch",
	"Accept-Language": "en-US,en;q=0.8",
	"Cache-Control": "max-age=0",
	"Connection": "keep-alive",
	"Host": "redrocksonline.com",
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36"
}

soup_page = []
#for fragment in ('', '/index/10', '/index/20', '/index/30', '/index/40'):
#url = ("http://redrocksonline.com/concerts-events/calendar")
req = Request("http://redrocksonline.com/concerts-events/calendar")
req.add_header('Referer', headers)
page = urlopen(req)
x = BeautifulSoup(page)
print(x)
'''