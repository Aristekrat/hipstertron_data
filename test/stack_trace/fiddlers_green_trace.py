import datetime

artists_stripped_chars = ['Darius Rucker', 'Train / The Fray', 'Fall Out Boy / Wiz Khalifa', 'Foo Fighters', 'Foo Fighters', 'Dave Matthews Band', 'Dave Matthews Band']

dates_culled = ['Jul 17,', 'Jul 18,', 'Jul 29,', 'Aug 16,', 'Aug 17,', 'Aug 28,', 'Aug 29,']

dates_stripped_chars = ['Jul 17', 'Jul 18', 'Jul 29', 'Aug 16', 'Aug 17', 'Aug 28', 'Aug 29']

dates_format_month = ['July 17', 'July 18', 'July 29', 'August 16', 'August 17', 'August 28', 'August 29']

dates_format_year = ['July 17 2015', 'July 18 2015', 'July 29 2015', 'August 16 2015', 'August 17 2015', 'August 28 2015', 'August 29 2015']

dates_datetime = [datetime.datetime(2015, 7, 17, 0, 0), datetime.datetime(2015, 7, 18, 0, 0), datetime.datetime(2015, 7, 29, 0, 0), datetime.datetime(2015, 8, 16, 0, 0), datetime.datetime(2015, 8, 17, 0, 0), datetime.datetime(2015, 8, 28, 0, 0), datetime.datetime(2015, 8, 29, 0, 0)]

ticket_links_raw = ['\n\t\t\n\t\t<a href="http://www.axs.com/events/268825/darius-rucker-tickets?skin=fiddlersgreen" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268401/train-the-fray-tickets?skin=fiddlersgreen" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268369/fall-out-boy-wiz-khalifa-tickets?skin=fiddlersgreen" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256532/foo-fighters-tickets?skin=fiddlersgreen" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256277/foo-fighters-tickets?skin=fiddlersgreen" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268332/dave-matthews-band-tickets?skin=fiddlersgreen" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268333/dave-matthews-band-tickets?skin=fiddlersgreen" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t']

ticket_links = ['http://www.axs.com/events/268825/darius-rucker-tickets?skin=fiddlersgreen', 'http://www.axs.com/events/268401/train-the-fray-tickets?skin=fiddlersgreen', 'http://www.axs.com/events/268369/fall-out-boy-wiz-khalifa-tickets?skin=fiddlersgreen', 'http://www.axs.com/events/256532/foo-fighters-tickets?skin=fiddlersgreen', 'http://www.axs.com/events/256277/foo-fighters-tickets?skin=fiddlersgreen', 'http://www.axs.com/events/268332/dave-matthews-band-tickets?skin=fiddlersgreen', 'http://www.axs.com/events/268333/dave-matthews-band-tickets?skin=fiddlersgreen']

ticket_prices_without_fees = ['25.00', '30.00', '20.00', '42.50', '42.50', '40.50', 0]

ticket_prices_patched = ['25.00', '30.00', '20.00', '42.50', '42.50', '40.50', 0]

ticket_prices = [33.75, 40.5, 27.6, 52.5, 52.5, 50.0, 0]