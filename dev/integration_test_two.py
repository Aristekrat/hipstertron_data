from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from time import strptime
import psycopg2

#This file tests submitting results to the database.  

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

# Get Urls and convert to soup object
def get_pages(urls):
	soup_page = []
	for url in urls:
		req = Request(url, headers = header)
		page = urlopen(req)
		soupified = BeautifulSoup(page)
		soup_page.append(soupified)
	return soup_page

gothic = get_pages(gothic_urls)


# Artist scraping section
def scrape_artists(pages, selector):
	scraped = []
	for page in pages:
		scraped.append(page.select(selector))
	return scraped

gothic_artists = scrape_artists(gothic, gothic_artist_selector)
gothic_artists = strip_html(gothic_artists)

# Dates scraping section

def scrape_dates(pages, selector):
	scraped = []
	for page in pages:
		date = page.select(selector)
		scraped.append(date)
	return scraped

gothic_dates = scrape_dates(gothic, gothic_date_selector)

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

gothic_dates = strip_unwanted_datechars(gothic_dates)
gothic_dates = strip_string_ends(gothic_dates, 4, 8)

#Works for Fillmore, haven't tested it with the others. 
def convert_to_datetime(results):
	converted = []
	for result in results:
		x = strptime(result, "%B %d %Y")
		converted.append(x)
	return converted

gothic_dates = convert_to_datetime(gothic_dates)

conn = psycopg2.connect("dbname='hipstertron' user='brian' host='localhost' password='412909AB'")

cur = conn.cursor()

def add_to_database(artists, dates):
	# This function works but does not preserve the date / datetime object. 
	i = 0
	while i < len(artists):
		cur.execute("INSERT INTO hello_gothic (artist, date) VALUES(%s, %s)", [artists[i], dates[i]])
		i = i +1
	#this actually works
	#for x in artists:
	#	cur.execute("INSERT INTO gothic_info (artist) VALUES(%s)", [x])

add_to_database(gothic_artists, gothic_dates)

def super_add(dates):
	for date in gothic_dates:
		sql_command = '''INSERT INTO gothic_info (date) VALUES ({})'''.format(date)
		cur.execute(sql_command)

#super_add(gothic_dates)

cur.close()

conn.commit()

conn.close()

