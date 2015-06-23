import datetime

artists_stripped_chars = ['Brian Wilson with special guest Rodriguez', '3 Doors Down / Seether', 'Jim Gaffigan', 'Zedd', 'Dancing with the Broomfield Stars', 'Of Monsters and Men']

dates_culled = ['Jul 8,', 'Jul 14,', 'Jul 29,', 'Sep 10,', 'Sep 24,', 'Oct 13,']

dates_stripped_chars = ['Jul 8', 'Jul 14', 'Jul 29', 'Sep 10', 'Sep 24', 'Oct 13']

dates_format_month = ['July 8', 'July 14', 'July 29', 'September 10', 'September 24', 'October 13']

dates_format_year = ['July 8 2015', 'July 14 2015', 'July 29 2015', 'September 10 2015', 'September 24 2015', 'October 13 2015']

dates_datetime = [datetime.datetime(2015, 7, 8, 0, 0), datetime.datetime(2015, 7, 14, 0, 0), datetime.datetime(2015, 7, 29, 0, 0), datetime.datetime(2015, 9, 10, 0, 0), datetime.datetime(2015, 9, 24, 0, 0), datetime.datetime(2015, 10, 13, 0, 0)]

ticket_links_raw = ['\n\t\t\n\t\t<a href="http://www.altitudetickets.com/event/rodriguez-brian-wilson-3622/" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.altitudetickets.com/event/3-doors-down-seether-3870/" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.altitudetickets.com/event/jim-gaffigan-3569/" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.altitudetickets.com/event/zedd-3914/" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.broomfieldfoundation.org/dancing-with-the-broomfield-stars" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.altitudetickets.com/event/of-monsters-and-men-3949/" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t']

ticket_links = ['http://www.altitudetickets.com/event/rodriguez-brian-wilson-3622/', 'http://www.altitudetickets.com/event/3-doors-down-seether-3870/', 'http://www.altitudetickets.com/event/jim-gaffigan-3569/', 'http://www.altitudetickets.com/event/zedd-3914/', 'http://www.broomfieldfoundation.org/dancing-with-the-broomfield-stars', 'http://www.altitudetickets.com/event/of-monsters-and-men-3949/']

ticket_prices_html = ['Tickets Starting at $49.75', 'Tickets starting at $35', 'Tickets starting at $59.60', 'Tickets starting at $20.00', 'Tickets starting at $35']

ticket_prices_without_fees = ['49.75', '35', '59.60', '20.00', '35']

ticket_prices_patched = ['49.75', '35', '59.60', '20.00', 0, '35']

ticket_prices = [61.25, 45.5, 70.8, 27.6, 0, 45.5]