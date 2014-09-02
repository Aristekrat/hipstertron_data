from time import strptime

#Scrapes dates from a Beautiful Soup object based on selector
def scrape_dates(pages, selector):
	scraped = []
	for page in pages:
		date = page.select(selector)
		scraped.append(date)
	return scraped

# Replaces newlines, tabs, commas
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

# Not working for all venues yet. Very particular about Month day year format. 
def convert_to_datetime(results):
	converted = []
	for result in results:
		x = strptime(result, "%B %d %Y")
		converted.append(x)
	return converted