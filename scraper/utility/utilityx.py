import sys
sys.path.append("../..")
from models import Denver_Concerts
from app import db

# AT - use regex to make sure no <tags> remain
def strip_html(results):
	stripped = []
	for result in results:
		for x in result:
			stripped.append(x.string)
	return stripped

# Try not to use this function if another will work. If the input changes it may break the code in confusing ways.
# TODO - when this function is used, test what chars it is removing
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


# Not sure how I would test this function, particularly in the abstract. Likely need a postgres mock
def add_concert_to_database(artists, dates, showLinks, id):
	for index, artist in enumerate(artists):
		if (dates[index] == None):
			continue
		else:
			new_show = Denver_Concerts(showDate = dates[index], band = artists[index], showLink = showLinks[index], concertVenueId = id)
			db.session.add(new_show)
		db.session.commit()

# This function can be applied to a huge range of scraping targets, but is prone to errors because the relative position of the correct text may change in the string
def lazy_strip(results, correctIndex):
	scraped = []
	for result in results: 
		x = result.split('"')
		scraped.append(x[correctIndex])
	return scraped 