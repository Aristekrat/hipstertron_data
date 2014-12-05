import re

# Applies to : Gothic, Ogden, Bluebird
# The site maintainers added an internal span which messed with BeautifulSoup's ability to access obj.string, which necessitated this site specific function
# def special_strip_html(results):
# 	stripped = []
# 	for result in results:
# 		for x in result:
# 			z = str(x)
# 			t = z.split()
# 			stripped_date = " ".join(t[6:9])
# 			stripped.append(stripped_date)
# 	return stripped

# Applies to : Fillmore
# The fillmore has relative links and it currently doesn't have a unique css selector for pages
# Thus, a site specific function is required
def scrape_concert_pages(root_page, root_url, selector):
	scraped = [root_url[0]]
	x = root_page[0].select(selector)
	for r in x:
		if r.string != ">":
			scraped.append("http://www.fillmoreauditorium.org" + r.attrs['href'])
	return scraped

# Applies to : Pepsi
# This function gets rid of the "Blah blah world tour" nonsense. It can probably be refactored into an all purpose artist filter
def pepsi_strip_artists(results):
	stripped = []
	for artist in results:
		x = re.split('[:"-]', artist)
		stripped.append(str(x[0]))
	return stripped

# I might be able to use this one as a template for my regex date searcher 
# def remove_listings_without_dates(dates_list, artists_list):
# 	stripped = []
# 	for index, date in enumerate(dates_list): 
# 		x = re.search('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec', date)
# 		if (x == None):
# 			artists_list.pop(index)
# 			continue
# 		else:
# 			stripped.append(x.string)
# 	return stripped

# Harvests the date from the string. By searching for the month and then adding the result that comes after it.
# # TODO - add a test that performs a findall for the date string and raises a warning if multiple months are found
# def cull_date_and_month(results):
# 	culled = []
# 	for date in results:
# 		string_date = str(date)
# 		components = string_date.split()
# 		for index, component in enumerate(components):
# 			x = re.search('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec', component)
# 			if (x):
# 				month_item = components[index]
# 				date_item = components[index + 1]
# 				standard_result = month_item + " " + date_item
# 				# This if block block detects date ranges, eg 2-5. I used the length property because most proper, non-range dates will have only a length of 2
# 				if (len(date_item) > 2):
# 					t = re.search('-', component)
# 					if (not t):
# 						culled.append(standard_result)
# 					else: 
# 						# Need a range handler function
# 						culled.append(month_item + " " + date_item[0])
# 				else: 
# 					culled.append(standard_result)
# 	return culled

# Applies to : Red Rocks
# Special Red Rocks functions
# If memory serves right, this is the explanation for these functions:
# Red Rocks doesn't list the date for the concert in plain text on the calendar. I can however follow the link to the concert details page and get the plain text page there
# This first function collects all the links
def get_redrocks_dateurls(results):
	dates = []
	for result in results: 
		for x in result:
			dates.append(x.attrs['href'])
	return dates

# This next function scrapes all the secondary pages
def scrape_redrocks_dates(pages): 
	scraped = []
	for page in pages:
		scraped.append(page.find(class_ = "date_time"))
	return scraped

# The selector gets too many results, so this function boots out the evenly spaced junk
def redrocks_strip_dates(results):
	i = 1
	stripped = []
	for result in results:
		if result and i % 2 == 0:
			stripped.append(result)
		i = i + 1
	return stripped