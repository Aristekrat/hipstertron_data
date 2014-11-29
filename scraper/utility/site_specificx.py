import re

# Applies to : Gothic, Ogden, Bluebird
# The site maintainers added an internal span which messed with BeautifulSoup's ability to access obj.string, which necessitated this site specific function
def special_strip_html(results):
	stripped = []
	for result in results:
		for x in result:
			z = str(x)
			t = z.split()
			stripped_date = " ".join(t[6:9])
			stripped.append(stripped_date)
	return stripped

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

# I didn't write an explanatory comment when I wrote this function so I'm not altogether sure why this is necessary
def fillmore_modify_string(results):
	stripped = []
	for result in results:
		result = result.split(' ')
		result.insert(-1, result[0])
		del result[0]
		stripped.append(" ".join(result))
	return stripped

# Applies to : Pepsi
# This function gets rid of the "Blah blah world tour" nonsense. It can probably be refactored into an all purpose artist filter
def pepsi_strip_artists(results):
	stripped = []
	for artist in results:
		x = re.split('[:"-]', artist)
		stripped.append(str(x[0]))
	return stripped

# I might be able to use this one as a template for my regex date searcher 
def get_proper_dates(results, artists_list):
	stripped = []
	for index, date in enumerate(results): 
		x = re.search('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec', date)
		if (x == None):
			artists_list.pop(index)
			continue
		else:
			stripped.append(x.string)
	return stripped

# Harvests the date from the string.
# A portion of this one should be combined with the date finder and the other portion should become the function that handles ranges
def cull_dates(results):
	culled = []
	for date in results:
		components = date.split()
		for index, component in enumerate(components):
			x = re.search('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec', component)
			if (x == None):
				continue
			elif (x != None):
				# This monkey patch handles ranges that are formatted as single strings, eg 6-8. Obviously, this is the code version of duct tape.
				if (len(components[index + 1]) > 2):
					culled.append(components[index] + " " + components[index + 1][0])
				else: 
					culled.append(components[index] + " " + components[index + 1])
				break
	return culled

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