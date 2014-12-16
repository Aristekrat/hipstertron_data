# Selector Library, a collection of CSS selectors for scraping concert listings with Beautiful Soup

gothic = {"artist": ".entry h3 a", "date": ".date", "page_url": ".final .number", "ticket_url": ".buttons" }

bluebird = {"artist": ".entry h3 a", "date": ".date", "page_url": ".final .number", "ticket_url": ".buttons"}

ogden = {"artist": ".entry h3 a", "date": ".date", "page_url": ".final .number", "ticket_url": ".buttons"}

fillmore = {"artist": ".eventInfo h3 a", "date": ".eventInfo strong", "page_url": "a.page-numbers", "ticket_url": ".buyNowTicket a"}

firstbank = {"artist": ".info h3 a", "date": ".date", "page_url": ".final .number", "ticket_url": ".buttons"}

fox = {"artist": ".billing", "month": ".datepart-container .month", "day": ".datepart-container .day", "page_url": "", "ticket_url": ".foxevent"}

red_rocks = {"artist": "li .concert", "date": "date_time", "page_url": "", "ticket_url": "li .concert"}

pepsi_center = {"artist": ".image-title a", "date": ".image-line2", "page_url": "", "ticket_url": ".caption .more_info a"}

paramount = {"artist": ".photo-meta-data h2 a", "date": ".photo-meta-data p", "page_url": "", "ticket_url": ".photo-meta-data h2 a"}