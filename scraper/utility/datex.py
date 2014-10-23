import time
from datetime import datetime

#Scrapes dates from a Beautiful Soup object with a css selector
def scrape_dates(pages, selector):
	scraped = []
	for page in pages:
		date = page.select(selector)
		scraped.append(date)
	return scraped

# Replaces newlines, tabs, commas, and periods with nothingness
def strip_unwanted_datechars(results):
	remap = {
		ord('\n') : None,
		ord('\t') : None,
		ord(',') : None,
		ord('.') : None
	}
	stripped = []
	for result in results:
		if result == None:
			result = ""
		stripped.append(result.translate(remap))
	return stripped

# Very particular about Month, day, year format. 
def convert_to_datetime(results):
	converted = []
	for result in results:
		concert_date = time.strptime(result, "%B %d %Y")
		today_string = time.strftime("%B %d %Y")
		today_datetime = time.strptime(today_string, "%B %d %Y")
		if (today_datetime > concert_date):
			concert_date = None
		else: 
			concert_date = datetime.fromtimestamp(time.mktime(concert_date))
		converted.append(concert_date)
	return converted

# Expands shortened month names
def format_months(results):
	formatted = []
	for date in results:
		components = date.split()
		month = components[0]
		if month == "Sept":
			month = "September"
		elif month == "Oct":
			month = "October"
		elif month == "Nov":
			month = "November"
		elif month == "Dec":
			month = "December"
		elif month == "Jan":
			month = "January"
		elif month == "Feb":
			month = "February"
		elif month == "Mar":
			month = "March"
		elif month == "Apr":
			month = "April"
		elif month == "Aug":
			month = "August"
		components[0] = month
		date = " ".join(components)
		formatted.append(date)
	return formatted

# Adds the correct year, NOTE this function requires the month be in the proper format first
def add_year(results):
	formatted = []
	for date in results: 
		components = date.split()
		month = components[0]
		if month == "September" or month == "October" or month == "November" or month == "December":
			year = " 2014"
		if month == "January" or month == "February" or month == "March" or month == "April" or month == "May" or month == "June" or month == "July" or month == "August":
			year = " 2015"
		formatted.append(date + year)
	return formatted