import time
from datetime import datetime

#Scrapes dates from a Beautiful Soup object with a css selector
#TODO - AT Test if not empty
#TODO - AT Test that none of the values are empty strings or None
def scrape_dates(pages, selector):
	scraped = []
	for page in pages:
		date = page.select(selector)
		scraped.append(date)
	return scraped

# Very particular about Month, day, year format.
def convert_to_datetime(results):
	converted = []
	today_string = time.strftime("%B %d %Y")
	today_datetime = time.strptime(today_string, "%B %d %Y")

	for index, result in enumerate(results):
		try: 
			concert_date = time.strptime(result, "%B %d %Y")
		except ValueError:
			print("Cannot convert '" + result + "' at item " + str(index) + ". This is the full list: " + results)
		else: 
			if (today_datetime > concert_date):
				concert_date = None
			else: 
				concert_date = datetime.fromtimestamp(time.mktime(concert_date))
			converted.append(concert_date)
	return converted

# Expands shortened month names
# TODO - Applied test this one by checking if component[0] equals one of the listed months.
# Note - May want to refactor the way this function handles an input error (in the else clause)
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

# Adds the correct year, this function requires the month be in the proper format first
# Q - what should this function do in case it receives invalid input? 
def add_year(results):
	formatted = []
	for date in results: 
		components = date.split()
		month = components[0]
		if month == "November" or month == "December":
			year = " 2014"
		elif month == "January" or month == "February" or month == "March" or month == "April" or month == "May" or month == "June" or month == "July" or month == "August" or "September" or month == "October":
			year = " 2015"
		formatted.append(date + year)
	return formatted