import re
import sys
sys.path.append("..")
from libraries import regex_library
from memory_profiler import profile

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

