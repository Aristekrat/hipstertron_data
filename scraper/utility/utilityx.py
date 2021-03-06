import re
import sys
sys.path.append("../..")
from models import Denver_Concerts
from app import db

# This function will offset from the beginning and offset from the end. Thus the args results, 1, 1 will start at the 1 char and slice off 1 char from the end. 
# Try not to use this function if another will work. If the input changes it may break the code in confusing ways.+
def strip_string_ends(results, beginning, end):
	stripped = []
	for result in results: 
		x = result[beginning:-end].strip()
		stripped.append(x)
	return stripped

def strip_unwanted_chars(results):
	stripped = []
	remap = {
		ord('\n') : None,
		ord('\t') : None,
		ord(',') : None,
		ord('.') : None
	}
	for result in results:
		stripped.append(result.translate(remap))
	return stripped

# This will change any weird capitalization to Title Case
def correct_capitalization(results):
	corrected = []
	for result in results:
		reset_string = result.lower()
		capitalized_first_letter = reset_string.title()
		corrected.append(capitalized_first_letter)
	return corrected 

# NOTE Not sure how I would test this function, particularly in the abstract. Likely need a postgres mock
def add_concert_to_database(mode, artists, dates, showLinks, ticketPrices, id):
	if (mode != "debug"):
		for index, artist in enumerate(artists):
			if (dates[index] == None):
				continue
			else:
				new_show = Denver_Concerts(showDate = dates[index], band = artists[index], showLink = showLinks[index], price = ticketPrices[index], concertVenueId = id)
				db.session.add(new_show)
			db.session.commit()

# This function can be applied to a huge range of scraping targets, but is prone to errors because the relative position of the correct text may change in the string
def lazy_strip(results, correctIndex):
	scraped = []
	for result in results: 
		x = result.split('"')
		scraped.append(x[correctIndex])
	return scraped 

# This function should be used in the dates section of the execution scripts
def remove_listings_without_dates(dates_list, artists_list):
	stripped = []
	for index, date in enumerate(dates_list): 
		x = re.search('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec', date)
		if (x == None):
			artists_list.pop(index)
			continue
		else:
			stripped.append(x.string)
	return stripped