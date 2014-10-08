import sys
import re
import calendar
sys.path.append("..")
from utility import sitex, artistx, datex, utilityx

#Fox Theater is a special little snowflake and works almost entirely differently from the other venues. Inspect the raw html to discover why.

urls = ["http://www.foxtheatre.com/"]

site_html = sitex.get_pages(urls)

site_html_stringed = str(site_html)
find_var_pattern = "\[(.*?)\]"
all_brackets = re.findall(find_var_pattern, site_html_stringed)

data_var = all_brackets.pop()

#Artists

find_bands_pattern = '"Billing":"(.*?)"'
artists_raw = re.findall(find_bands_pattern, data_var)

def format_artists(results):
	formatted = []
	for result in results:
		#This method of replacing the unicode character's is weird and inefficient, but nothing else worked for me. 
		x = result.replace('\\u0026', '&')
		x = x.replace("\\u0027", "'")
		t = x[0] + x[1:].lower()
		formatted.append(t)
	return formatted

artists_stripped = format_artists(artists_raw)

#Dates

find_dates_pattern = '"SortTime":"(.*?)"'
dates_raw = re.findall(find_dates_pattern, data_var)

def remove_times(results):
	stripped = []
	for result in results:
		t = result.split(" ")
		stripped.append(t[0])
	return stripped

dates_filtered = remove_times(dates_raw)

def format_dates(results):
	formatted = []
	for result in results: 
		new_date = [None] * 3
		old_date = result.split("/")
		new_date[2] = old_date[0] #Year
		new_date[1] = old_date[2] #Day
		t = int(old_date[1])
		new_date[0] = calendar.month_name[t]
		full_date = " ".join(new_date)
		formatted.append(full_date)

	return formatted

dates_formatted = format_dates(dates_filtered)

dates_datetime = datex.convert_to_datetime(dates_formatted)

#print(dates_datetime)

#utilityx.add_concert_to_database(artists_stripped, dates_datetime, 10)
