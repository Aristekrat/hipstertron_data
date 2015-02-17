import re
import sys
sys.path.append("..")
from libraries import regex_library

#Pretty similar to the artist scraping function, it just involves an additional for loop.
#Can this be converted into a generic link scraping function? Maybe combined with the function below as well
def scrape_concert_links(pages, selector):
	scraped = []
	for page in pages:
		x = page.select(selector)
		for r in x:
			scraped.append(r.attrs['href'])
	return scraped

# This function will only work with bs4 objects. Evidently it is only used with Red Rocks.
def scrape_links_from_result_set(results):
	scraped = []
	for result in results:
		for r in result:
			scraped.append(r.attrs['href'])
	return scraped

def remove_duplicates(li):
    my_set = set()
    res = []
    for e in li:
        if e not in my_set:
            res.append(e)
            my_set.add(e)
    return res

#Gets full urls dynamically for concert listings with pagination
def scrape_concert_pages(root_page, root_url, selector):
	scraped = [root_url[0]]
	x = root_page[0].select(selector)
	for r in x:
		scraped.append(r.attrs['href'])
	return scraped

# Used for completing relative links
def ticket_link_prefix(prefix, results):
	formatted = []
	for result in results: 
		full_url = prefix + result
		formatted.append(full_url)
	return formatted

# Needs tests
def scrape_hrefs(results):
	scraped = []
	re_href = regex_library.patterns["href"]
	for result in results:
		search_result = re_href.search(result)
		if search_result:
			t = search_result.group()
			t = t[6:]
			scraped.append(t)
	return scraped

# Needs tests 
def filter_urls(results):
	filtered = []
	re_urls = regex_library.patterns["urls"]
	for result in results: 
		search_result = re_urls.search(result)
		if search_result:
			filtered.append(search_result.group())
		else: 
			filtered.append("javascript:void(0);")
	return filtered

# This function adds 0 to shows without a valid url
def patch_bad_urls(ticket_links, ticket_prices):
	re_urls = regex_library.patterns["urls"]
	for index, link in enumerate(ticket_links):
		search_result = re_urls.search(link)
		if not search_result:
			ticket_prices.insert(index, 0)
	return ticket_prices
	
# This function adds 0 to shows when BS4 wasn't able to find pricing information after following the link
def patch_no_results_found(bs4_results, ticket_prices):
	for index, result in enumerate(bs4_results):
		if not result:
			ticket_prices.insert(index, 0)
	return ticket_prices

# Applies all patch types
def patch_prices(ticket_links, bs4_results, ticket_prices):
	t = patch_bad_urls(ticket_links, ticket_prices)
	patched = patch_no_results_found(bs4_results, t)
	return patched

#This function should be able to find any price formatted like so: $35, $35.00, $3.00, $3000.00. It won't find a price without a $
#TODO needs a unittest. 
def find_prices(results):
	ticket_prices = []
	re_price = regex_library.patterns["price"]
	# TODO - I either need to filter input or split off some of this logic. This function currently does too much. 
	for result in results:
		if type(result) is list and result:
			try: 
				t = re_price.search(str(result[0]))
				if t:
					x = t.group()
					x = x[1:]
					ticket_prices.append(x)
				else: 
					ticket_prices.append(0)
			except:
				continue 
		else:
			try: 
				t = re_price.search(str(result))
				if t: 
					x = t.group()
					x = x[1:]
					ticket_prices.append(x)
				else:
					ticket_prices.append(0)
			except:
				continue
			# 	ticket_prices.append(0)
	return ticket_prices

# Omg tests
def calculate_rate(number, rate):
	unrounded = number * rate
	rounded = round(unrounded, 2)
	return rounded

# Needs tests
def add_fee_estimate(results):
	ticket_prices = []
	for result in results:
		try:
			t = int(float(result))
			if t == 0:
				ticket_prices.append(0)
			elif t < 25:
				ticket_prices.append(calculate_rate(t, 1.38))
			elif t < 31 and t >= 25:
				ticket_prices.append(calculate_rate(t, 1.35))
			elif t < 39 and t >= 31:
				ticket_prices.append(calculate_rate(t, 1.30))
			elif t < 50 and t >= 39:
				ticket_prices.append(calculate_rate(t, 1.25))
			elif t < 80 and t >= 50:
				ticket_prices.append(calculate_rate(t, 1.20))
			elif t >= 80:
				ticket_prices.append(calculate_rate(t, 1.17))
		except:
			ticket_prices.append(0)
			continue
	return ticket_prices

def no_prices(results):
	no_prices = []
	for result in results:
		no_prices.append(0)
	return no_prices