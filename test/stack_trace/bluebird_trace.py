import datetime

artists_stripped_chars = ['Jeff Austin Band feat Jeff Austin formerly of Yonder Mountain String Band', 'Wild Child', 'Todd Snider', 'Cursive', 'RAH', 'Mountain Standard Time', 'Ariel Pink', "Hot Soup does 'Chocolate and Cheese' (Ween)", 'Kina Grannis', 'Saints of Valory', 'Stelth Ulvang (of The Lumineers)', "Cash'd Out (The Ultimate Johnny Cash Tribute)", 'Hundred Waters', 'Theophilus London', 'Milo Greene', 'Houndmouth', 'Flight Facilities', 'Prhyme (Royce da 5′9″ and DJ Premier)', 'The 3hree Project Soundstage ft the live performance of the 3hree Project Album with special guests', 'YAMN', 'Analog Son Album Release with Very Special Guests Nigel Hall (Lettuce Soulive Nth Power) and Jason Hann (SCI EOTO)', 'MisterWives', 'Common Kings', 'Doro', 'Mile High Sound Orchestra', 'Manic Focus', 'BROODS', 'Mlima', 'The Dodos', 'Goldfish', 'The Congress', 'Magic Man', 'Trout Steak Revival', 'Hurray for the Riff Raff', 'The London Souls / Sons of Bill', 'Generationals', 'of Montreal', 'Stars', 'Joe Pug', "The Reverend Peyton's Big Damn Band"]

dates_culled = ['Feb 6,', 'Feb 7,', 'Feb 9,', 'Feb 10,', 'Feb 12,', 'Feb 13,', 'Feb 14,', 'Feb 15,', 'Feb 17,', 'Feb 18,', 'Feb 19,', 'Feb 20,', 'Feb 21,', 'Feb 26,', 'Feb 27,', 'Feb 28,', 'Mar 2,', 'Mar 3,', 'Mar 4,', 'Mar 6,', 'Mar 7,', 'Mar 9,', 'Mar 10,', 'Mar 11,', 'Mar 12,', 'Mar 13,', 'Mar 14,', 'Mar 15,', 'Mar 16,', 'Mar 20,', 'Mar 21,', 'Mar 23,', 'Mar 26,', 'Mar 27,', 'Mar 28,', 'Mar 30,', 'Mar 31,', 'Apr 1,', 'Apr 3,', 'Apr 4,']

dates_stripped_chars = ['Feb 6', 'Feb 7', 'Feb 9', 'Feb 10', 'Feb 12', 'Feb 13', 'Feb 14', 'Feb 15', 'Feb 17', 'Feb 18', 'Feb 19', 'Feb 20', 'Feb 21', 'Feb 26', 'Feb 27', 'Feb 28', 'Mar 2', 'Mar 3', 'Mar 4', 'Mar 6', 'Mar 7', 'Mar 9', 'Mar 10', 'Mar 11', 'Mar 12', 'Mar 13', 'Mar 14', 'Mar 15', 'Mar 16', 'Mar 20', 'Mar 21', 'Mar 23', 'Mar 26', 'Mar 27', 'Mar 28', 'Mar 30', 'Mar 31', 'Apr 1', 'Apr 3', 'Apr 4']

dates_format_month = ['February 6', 'February 7', 'February 9', 'February 10', 'February 12', 'February 13', 'February 14', 'February 15', 'February 17', 'February 18', 'February 19', 'February 20', 'February 21', 'February 26', 'February 27', 'February 28', 'March 2', 'March 3', 'March 4', 'March 6', 'March 7', 'March 9', 'March 10', 'March 11', 'March 12', 'March 13', 'March 14', 'March 15', 'March 16', 'March 20', 'March 21', 'March 23', 'March 26', 'March 27', 'March 28', 'March 30', 'March 31', 'April 1', 'April 3', 'April 4']

dates_format_year = ['February 6 2015', 'February 7 2015', 'February 9 2015', 'February 10 2015', 'February 12 2015', 'February 13 2015', 'February 14 2015', 'February 15 2015', 'February 17 2015', 'February 18 2015', 'February 19 2015', 'February 20 2015', 'February 21 2015', 'February 26 2015', 'February 27 2015', 'February 28 2015', 'March 2 2015', 'March 3 2015', 'March 4 2015', 'March 6 2015', 'March 7 2015', 'March 9 2015', 'March 10 2015', 'March 11 2015', 'March 12 2015', 'March 13 2015', 'March 14 2015', 'March 15 2015', 'March 16 2015', 'March 20 2015', 'March 21 2015', 'March 23 2015', 'March 26 2015', 'March 27 2015', 'March 28 2015', 'March 30 2015', 'March 31 2015', 'April 1 2015', 'April 3 2015', 'April 4 2015']

dates_datetime = [datetime.datetime(2015, 2, 6, 0, 0), datetime.datetime(2015, 2, 7, 0, 0), datetime.datetime(2015, 2, 9, 0, 0), datetime.datetime(2015, 2, 10, 0, 0), datetime.datetime(2015, 2, 12, 0, 0), datetime.datetime(2015, 2, 13, 0, 0), datetime.datetime(2015, 2, 14, 0, 0), datetime.datetime(2015, 2, 15, 0, 0), datetime.datetime(2015, 2, 17, 0, 0), datetime.datetime(2015, 2, 18, 0, 0), datetime.datetime(2015, 2, 19, 0, 0), datetime.datetime(2015, 2, 20, 0, 0), datetime.datetime(2015, 2, 21, 0, 0), datetime.datetime(2015, 2, 26, 0, 0), datetime.datetime(2015, 2, 27, 0, 0), datetime.datetime(2015, 2, 28, 0, 0), datetime.datetime(2015, 3, 2, 0, 0), datetime.datetime(2015, 3, 3, 0, 0), datetime.datetime(2015, 3, 4, 0, 0), datetime.datetime(2015, 3, 6, 0, 0), datetime.datetime(2015, 3, 7, 0, 0), datetime.datetime(2015, 3, 9, 0, 0), datetime.datetime(2015, 3, 10, 0, 0), datetime.datetime(2015, 3, 11, 0, 0), datetime.datetime(2015, 3, 12, 0, 0), datetime.datetime(2015, 3, 13, 0, 0), datetime.datetime(2015, 3, 14, 0, 0), datetime.datetime(2015, 3, 15, 0, 0), datetime.datetime(2015, 3, 16, 0, 0), datetime.datetime(2015, 3, 20, 0, 0), datetime.datetime(2015, 3, 21, 0, 0), datetime.datetime(2015, 3, 23, 0, 0), datetime.datetime(2015, 3, 26, 0, 0), datetime.datetime(2015, 3, 27, 0, 0), datetime.datetime(2015, 3, 28, 0, 0), datetime.datetime(2015, 3, 30, 0, 0), datetime.datetime(2015, 3, 31, 0, 0), datetime.datetime(2015, 4, 1, 0, 0), datetime.datetime(2015, 4, 3, 0, 0), datetime.datetime(2015, 4, 4, 0, 0)]

ticket_links_raw = ['\n\t\t\n\t\t<a href="http://www.axs.com/events/255891/jeff-austin-band-feat-jeff-austin-formerly-of-yonder-mountain-string-b-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255006/wild-child-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256501/todd-snider-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/254945/cursive-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/267777/rah-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/257126/mountain-standard-time-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255219/ariel-pink-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256970/hot-soup-does-chocolate-and-cheese-ween-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256783/kina-grannis-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256715/saints-of-valory-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256643/stelth-ulvang-of-the-lumineers-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/267750/cash-d-out-the-ultimate-johnny-cash-tribute-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256236/hundred-waters-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256716/theophilus-london-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255333/milo-greene-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256134/houndmouth-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/257127/flight-facilities-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256636/prhyme-royce-da-5y9y-and-dj-premier-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268815/the-3hree-project-soundstage-ft-the-live-performance-of-the-3hree-proj-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256637/yamn-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/257114/analog-son-album-release-with-very-special-guests-nigel-hall-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256708/misterwives-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/267646/common-kings-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/254847/doro-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268802/mile-high-sound-orchestra-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268627/manic-focus-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256834/broods-tickets?skin=bluebird" title="Sold Out" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_7"><i class="fa fa-ticket fa-secondary"></i>Sold Out</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268826/mlima-tickets?skin=bluebird" title="On Sale Soon" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1 onsalesoon"><i class="fa fa-ticket fa-secondary"></i>On Sale Soon</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256137/the-dodos-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268486/goldfish-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268400/the-congress-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/267770/magic-man-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/267433/trout-steak-revival-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256662/hurray-for-the-riff-raff-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268317/the-london-souls-sons-of-bill-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268740/generationals-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268335/of-montreal-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255959/stars-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/268596/joe-pug-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256919/the-reverend-peyton-s-big-damn-band-tickets?skin=bluebird" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t']

ticket_links = ['http://www.axs.com/events/255891/jeff-austin-band-feat-jeff-austin-formerly-of-yonder-mountain-string-b-tickets?skin=bluebird', 'http://www.axs.com/events/255006/wild-child-tickets?skin=bluebird', 'http://www.axs.com/events/256501/todd-snider-tickets?skin=bluebird', 'http://www.axs.com/events/254945/cursive-tickets?skin=bluebird', 'http://www.axs.com/events/267777/rah-tickets?skin=bluebird', 'http://www.axs.com/events/257126/mountain-standard-time-tickets?skin=bluebird', 'http://www.axs.com/events/255219/ariel-pink-tickets?skin=bluebird', 'http://www.axs.com/events/256970/hot-soup-does-chocolate-and-cheese-ween-tickets?skin=bluebird', 'http://www.axs.com/events/256783/kina-grannis-tickets?skin=bluebird', 'http://www.axs.com/events/256715/saints-of-valory-tickets?skin=bluebird', 'http://www.axs.com/events/256643/stelth-ulvang-of-the-lumineers-tickets?skin=bluebird', 'http://www.axs.com/events/267750/cash-d-out-the-ultimate-johnny-cash-tribute-tickets?skin=bluebird', 'http://www.axs.com/events/256236/hundred-waters-tickets?skin=bluebird', 'http://www.axs.com/events/256716/theophilus-london-tickets?skin=bluebird', 'http://www.axs.com/events/255333/milo-greene-tickets?skin=bluebird', 'http://www.axs.com/events/256134/houndmouth-tickets?skin=bluebird', 'http://www.axs.com/events/257127/flight-facilities-tickets?skin=bluebird', 'http://www.axs.com/events/256636/prhyme-royce-da-5y9y-and-dj-premier-tickets?skin=bluebird', 'http://www.axs.com/events/268815/the-3hree-project-soundstage-ft-the-live-performance-of-the-3hree-proj-tickets?skin=bluebird', 'http://www.axs.com/events/256637/yamn-tickets?skin=bluebird', 'http://www.axs.com/events/257114/analog-son-album-release-with-very-special-guests-nigel-hall-tickets?skin=bluebird', 'http://www.axs.com/events/256708/misterwives-tickets?skin=bluebird', 'http://www.axs.com/events/267646/common-kings-tickets?skin=bluebird', 'http://www.axs.com/events/254847/doro-tickets?skin=bluebird', 'http://www.axs.com/events/268802/mile-high-sound-orchestra-tickets?skin=bluebird', 'http://www.axs.com/events/268627/manic-focus-tickets?skin=bluebird', 'http://www.axs.com/events/256834/broods-tickets?skin=bluebird', 'http://www.axs.com/events/268826/mlima-tickets?skin=bluebird', 'http://www.axs.com/events/256137/the-dodos-tickets?skin=bluebird', 'http://www.axs.com/events/268486/goldfish-tickets?skin=bluebird', 'http://www.axs.com/events/268400/the-congress-tickets?skin=bluebird', 'http://www.axs.com/events/267770/magic-man-tickets?skin=bluebird', 'http://www.axs.com/events/267433/trout-steak-revival-tickets?skin=bluebird', 'http://www.axs.com/events/256662/hurray-for-the-riff-raff-tickets?skin=bluebird', 'http://www.axs.com/events/268317/the-london-souls-sons-of-bill-tickets?skin=bluebird', 'http://www.axs.com/events/268740/generationals-tickets?skin=bluebird', 'http://www.axs.com/events/268335/of-montreal-tickets?skin=bluebird', 'http://www.axs.com/events/255959/stars-tickets?skin=bluebird', 'http://www.axs.com/events/268596/joe-pug-tickets?skin=bluebird', 'http://www.axs.com/events/256919/the-reverend-peyton-s-big-damn-band-tickets?skin=bluebird']

ticket_prices_without_fees = ['23.00', '13.00', '25.00', '18.00', '10.00', '10.00', '22.00', '10.00', '23.75', '13.50', '10.00', '10.00', '13.00', '19.99', '16.50', '15.00', '20.00', '15.00', '13.00', '5.00', '12.00', '5.00', '15.00', '20.00', '10.00', '15.00', '18.00', '10.00', '15.75', '15.00', '5.00', '10.00', '10.00', '15.00', '10.00', '10.00', '15.00', '23.00', '15.00', '16.50']

ticket_prices_patched = ['23.00', '13.00', '25.00', '18.00', '10.00', '10.00', '22.00', '10.00', '23.75', '13.50', '10.00', '10.00', '13.00', '19.99', '16.50', '15.00', '20.00', '15.00', '13.00', '5.00', '12.00', '5.00', '15.00', '20.00', '10.00', '15.00', '18.00', '10.00', '15.75', '15.00', '5.00', '10.00', '10.00', '15.00', '10.00', '10.00', '15.00', '23.00', '15.00', '16.50']

ticket_prices = [31.74, 17.94, 33.75, 24.84, 13.8, 13.8, 30.36, 13.8, 31.74, 17.94, 13.8, 13.8, 17.94, 26.22, 22.08, 20.7, 27.6, 20.7, 17.94, 6.9, 16.56, 6.9, 20.7, 27.6, 13.8, 20.7, 24.84, 13.8, 20.7, 20.7, 6.9, 13.8, 13.8, 20.7, 13.8, 13.8, 20.7, 31.74, 20.7, 22.08]