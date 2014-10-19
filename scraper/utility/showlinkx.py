#Pretty similar to the artist scraping function, it just involves an additional for loop.
def scrape_concert_links(pages, selector):
	scraped = []
	for page in pages:
		x = page.select(selector)
		for r in x:
			scraped.append(r.attrs['href'])
	return scraped