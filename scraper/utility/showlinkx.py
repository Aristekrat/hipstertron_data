#Pretty similar to the artist scraping function, it just involves an additional for loop.
#Can this be converted into a generic link scraping function? Maybe combined with the function below as well
def scrape_concert_links(pages, selector):
	scraped = []
	for page in pages:
		x = page.select(selector)
		for r in x:
			scraped.append(r.attrs['href'])
	return scraped

#Gets full urls dynamically for concert listings with pagination
def scrape_concert_pages(root_page, root_url, selector):
	scraped = [root_url[0]]
	x = root_page[0].select(selector)
	for r in x:
		scraped.append(r.attrs['href'])
	return scraped