import datetime

artists_stripped_chars = ['UFC Fight Night Henderson vs Thatch', 'Harlem Globetrotters', 'Dada Life', '6th annual Frank Shorter RACE', 'Volbeat']

dates_culled = ['Feb 14,', 'Mar 7,', 'Mar 13,', 'Apr 12,', 'Apr 24,']

dates_stripped_chars = ['Feb 14', 'Mar 7', 'Mar 13', 'Apr 12', 'Apr 24']

dates_format_month = ['February 14', 'March 7', 'March 13', 'April 12', 'April 24']

dates_format_year = ['February 14 2015', 'March 7 2015', 'March 13 2015', 'April 12 2015', 'April 24 2015']

dates_datetime = [datetime.datetime(2015, 2, 14, 0, 0), datetime.datetime(2015, 3, 7, 0, 0), datetime.datetime(2015, 3, 13, 0, 0), datetime.datetime(2015, 4, 12, 0, 0), datetime.datetime(2015, 4, 24, 0, 0)]

ticket_links_raw = ['\n\t\t\n\t\t<a href="http://www.altitudetickets.com/event/ufc-fight-night-3209/" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.altitudetickets.com/event/harlem-globetrotters-3008/" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.altitudetickets.com/event/dada-life-3358/" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.runningguru.com/EventInformation.asp?SourceCode=Search&amp;eID=12791" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.altitudetickets.com/event/volbeat-3153/" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t']

ticket_links = ['http://www.altitudetickets.com/event/ufc-fight-night-3209/', 'http://www.altitudetickets.com/event/harlem-globetrotters-3008/', 'http://www.altitudetickets.com/event/dada-life-3358/', 'http://www.runningguru.com/EventInformation.asp?SourceCode=Search&amp;eID=12791', 'http://www.altitudetickets.com/event/volbeat-3153/']

ticket_prices_html = ['Tickets Starting at $50', 'Tickets starting at $19', 'Tickets starting at $20', 'Tickets are $39.50']

ticket_prices_without_fees = ['50', '19', '20', '39.50']

ticket_prices_patched = ['50', '19', '20', 0, '39.50']

ticket_prices = [60.0, 26.22, 27.6, 0, 48.75]