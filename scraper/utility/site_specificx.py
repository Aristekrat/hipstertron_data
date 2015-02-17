import re

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

# Applies to : Fox
# Fox Theater has the month and date seperately, this function combines them
def combine(first_set, second_set):
	combined = []
	if len(first_set) == len(second_set):
		for index, result in enumerate(first_set):
			t = first_set[index] + " " + second_set[index]
			combined.append(t)
		return combined
	else:
		raise ValueError ("One set is longer than the other!")

# Applies to : Pepsi
# # This function gets rid of the "Blah blah world tour" nonsense. It can probably be refactored into an all purpose artist filter
# def pepsi_strip_artists(results):
# 	stripped = []
# 	for artist in results:
# 		x = re.split('[:"-]', artist)
# 		stripped.append(str(x[0]))
# 	return stripped

# def swift_fix(results):
# 	results.insert(-1, "javascript:void(0);")

# Applies to : Red Rocks
# Red Rocks ticket prices are hidden in a big lump of text. I use this function to extract the correct lump. 
def split_prices_text(results):
	prices = []
	for result in results:
		if result:
			x = re.split('\$', str(result))
			if len(x) >= 2:
				prices.append(x[1])
			else:
				prices.append("Unavailable")
	return prices