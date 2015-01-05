from defusedxml.ElementTree import parse
from collections import Counter
import sys
sys.path.append("..")
from models import User_Music
from app import db

parsed_file = parse("itunes.xml")

root = parsed_file.getroot()

listings = root.findall('dict/dict/dict')

def parse_iTunes(listings):
	parsed = []
	for listing in listings:
		for index, child in enumerate(listing):
			if child.text == "Artist":
				parsed.append(listing[index + 1].text)
	return parsed

parsed_results = parse_iTunes(listings)

counted_results = Counter(parsed_results)

sorted_results = sorted(counted_results.items(), key=lambda x:x[1])
sorted_results.reverse()

def add_user_music_to_database(results):
	for result in results:
		band = User_Music(artistName = result[0], count = result[1], userId = "6acebe51-1c90-4dd8-828f-d1c13d52f743")
		db.session.add(band)
	db.session.commit()

add_user_music_to_database(sorted_results)

# def add_user_music_to_database(results):
# 	for key in results.keys():
# 		band = User_Music(artistName = key, count = results[key], userId = "6acebe51-1c90-4dd8-828f-d1c13d52f743")
# 		db.session.add(band)
# 	db.session.commit()

# add_user_music_to_database(counted_results)