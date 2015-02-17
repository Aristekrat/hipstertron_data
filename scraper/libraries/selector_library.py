# Selector Library, a collection of CSS selectors for scraping concert listings with Beautiful Soup

gothic = {"artist": ".entry h3 a", "date": ".date", "page_url": ".final .number", "ticket_url": ".buttons", "ticket_price": "#admission-box .content-module-content div:nth-of-type(3)" }

bluebird = {"artist": ".entry h3 a", "date": ".date", "page_url": ".final .number", "ticket_url": ".buttons", "ticket_price": "#admission-box .content-module-content div:nth-of-type(3)"}

ogden = {"artist": ".entry h3 a", "date": ".date", "page_url": ".final .number", "ticket_url": ".buttons", "ticket_price": "#admission-box .content-module-content div:nth-of-type(3)"}

fillmore = {"artist": ".eventInfo h3 a", "date": ".eventInfo strong", "page_url": "a.page-numbers", "ticket_url": ".buyNowTicket a"}

first_bank = {"artist": ".info h3 a", "date": ".date", "page_url": ".final .number", "ticket_url": ".buttons", "ticket_price": ".buy-options-box h3:nth-of-type(1)"}

fiddlers_green = {"artist": ".carousel_item_title_small a", "date": ".date", "ticket_url": ".buttons", "ticket_price": "#admission-box .content-module-content div:nth-of-type(3)"}

fox = {"artist": ".billing", "month": ".datepart-container .month", "day": ".datepart-container .day", "page_url": "", "ticket_url": ".foxevent", "ticket_price": ".event-pricing span"}

red_rocks = {"artist": "li .concert", "date": "date_time", "page_url": "", "ticket_url": "li .concert", "ticket_price": ".fc_txt.fullpage"}

pepsi_center = {"artist": ".image-title a", "date": ".image-line2", "page_url": "", "ticket_url": ".caption .more_info a", "ticket_price": ".buy-options-box h3:nth-of-type(1)"}

#paramount = {"artist": ".photo-meta-data h2 a", "date": ".photo-meta-data p", "page_url": "", "ticket_url": ".photo-meta-data h2 a", "ticket_price": ".buy-options-box h3:nth-of-type(1)"}
paramount = {"artist": ".event-title h3", "date": ".panel-body p strong", "page_url": "", "ticket_url": ".feature-buttons", "ticket_price": ".buy-options-box h3:nth-of-type(1)"}

# summit = {"artist": ".blogSection tr:nth-of-type(2) td a", "date": "", "page_url": "", "ticket_url": "", "ticket_price": ""}

# marquis = {"artist": ".blogSection tr:nth-of-type(2) td a", "date": ".blogSection tr td span:nth-of-type(1)", "page_url": "", "ticket_url": "", "ticket_price": ""}