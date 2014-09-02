'''
foxtheatre_urls = ["http://www.foxtheatre.com/"]

# Fox Theatre
# Looking for: a javascript array named events. You need the SortTime and Billing fields. 
def get_page():
	soup_page = []
	url = ("http://www.foxtheatre.com/")
	page = urlopen(url)
	soup_page = BeautifulSoup(page)
	return soup_page

fox = get_page()

print(fox)
'''