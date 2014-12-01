import time
import re
from datetime import datetime

#Scrapes dates from a Beautiful Soup object with a css selector
#TODO - AT Test if not empty
#TODO - AT Test that none of the values are empty strings or None
# def scrape_dates(pages, selector):
# 	scraped = []
# 	for page in pages:
# 		date = page.select(selector)
# 		scraped.append(date)
# 	return scraped

# Harvests the date from the string. By searching for the month and then adding the result that comes after it.
# TODO - add a test that performs a findall for the date string and raises a warning if multiple months are found
def cull_date_and_month(results):
	culled = []
	for date in results:
		string_date = str(date)
		components = string_date.split()
		
		for index, component in enumerate(components):
			x = re.search('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec', component)
			if (x):
				month_item = components[index]
				date_item = components[index + 1]
				standard_result = month_item + " " + date_item
				# This if block block detects date ranges, eg 2-5. I used the length property because most proper, non-range dates will have only a length of 2
				if (len(date_item) > 2):
					t = re.search('\-', date_item)
					if (not t):
						culled.append(standard_result)
						break
					else: 
						# Need a range handler function
						culled.append(month_item + " " + date_item[0])
						break
				else: 
					culled.append(standard_result)
					break
	
	return culled

# For dates that are formatted : 12 December 2014, this function will convert that date into December 12 2014
def move_date_behind_month(results):
	stripped = []
	for result in results:
		result = result.split(' ')
		result.insert(-1, result[0])
		del result[0]
		stripped.append(" ".join(result))
	return stripped

# Very particular about Month, day, year format.
def convert_to_datetime(results):
	converted = []
	today_string = time.strftime("%B %d %Y")
	today_datetime = time.strptime(today_string, "%B %d %Y")

	for index, result in enumerate(results):
		try: 
			concert_date = time.strptime(result, "%B %d %Y")
		except ValueError:
			print("Cannot convert '" + result + "' at item " + str(index) + ". This is the full list: " + str(results))
			break
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
# TODO - refactor this one so it doesn't rely on the month being in position zero? Currently prone to breaking. Not releveant if always receives prepared input beforehand.
# TODO - use a month dictionary to shorten this function. You don't need this massive pile of if statements
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
# Change this function to dynamically detect the year
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