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

# Not sure how I would test this function, particularly in the abstract. Likely need a postgres mock
def add_concert_to_database(artists, dates, showLinks, id):
	# if (len(artists) == len(dates)):
	for index, artist in enumerate(artists):
		if (dates[index] == None):
			continue
		else:
			new_show = Denver_Concerts(showDate = dates[index], band = artists[index], showLink = showLinks[index], concertVenueId = id)
			db.session.add(new_show)
		db.session.commit()
	# else:
	# 	print("Error! Artist list and dates list are not the same length for venue: %s!" % id)
	# 	print("Artists length is: %s" % (len(artists)))
	# 	print("Dates length is: %s" % (len(dates)))