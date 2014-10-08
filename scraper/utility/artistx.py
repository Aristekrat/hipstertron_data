def scrape_artists(pages, selector):
	scraped = []
	for page in pages:
		scraped.append(page.select(selector))
	return scraped