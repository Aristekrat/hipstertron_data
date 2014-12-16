#Pretty similar to the artist scraping function, it just involves an additional for loop.
#Can this be converted into a generic link scraping function? Maybe combined with the function below as well
def scrape_concert_links(pages, selector):
	scraped = []
	for page in pages:
		x = page.select(selector)
		for r in x:
			scraped.append(r.attrs['href'])
	return scraped

# This function will only work with bs4 objects
def scrape_links_from_result_set(results):
	scraped = []
	for result in results:
		for r in result:
			scraped.append(r.attrs['href'])
	return scraped

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

# Someday I'll need a function that can use the artist list to search the links and determine which artist is missing a link
# However, it's not needed right now, so I created a far easier and lazier solution that pads out the links list with blank hrefs
def lazy_links_patch(artists, links):
	if (len(artists) > len(links)):
		deficiency = len(artists) - len(links)
		for d in deficiency:
			links.append("javascript:void(0);")
	return links