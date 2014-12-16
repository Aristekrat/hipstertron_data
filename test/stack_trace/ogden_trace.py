import datetime

artists_stripped_chars = ['Nathaniel Rateliff / Nathaniel Rateliff and the Night Sweats', 'BoomBox', 'BoomBox', 'Trombone Shorty &amp; Orleans Avenue', 'BoomBox', 'G-Eazy', 'Mac Miller', "Who's Bad: The World's #1 Michael Jackson Tribute Band", 'Colorado Up! The Inaugural Concert', 'Reel Big Fish / Less Than Jake', 'Guster', 'Cold War Kids', 'Railroad Earth', 'Railroad Earth', 'Railroad Earth', 'The Floozies', 'Logic', 'Bush', 'moe', 'moe', 'Borgore', 'Sleater‐Kinney', "Joe Russo's Almost Dead", "Joe Russo's Almost Dead", 'Hozier', 'Dr Dog', 'GALACTIC', 'GALACTIC', "Gov't Mule with Special Guest John Scofield", 'Iration', 'The New Deal', 'Gregory Alan Isakov', 'DATSIK', 'DATSIK', 'Twiddle', 'Mat Kearney', 'Sam Hunt', 'The Gaslight Anthem', 'TV On The Radio', 'Dan + Shay', 'The Sing-Off Live', 'Punch Brothers', 'Father John Misty', 'North Mississippi Allstars / Anders Osborne Present NMO', 'Sixx:AM', 'Nightwish', 'Milky Chance', 'OK Go', 'Kamelot']

dates_culled = ['Dec 19,', 'Dec 26,', 'Dec 27,', 'Dec 28,', 'Dec 31,', 'Jan 5,', 'Jan 9,', 'Jan 10,', 'Jan 13,', 'Jan 15,', 'Jan 17,', 'Jan 21,', 'Jan 22,', 'Jan 23,', 'Jan 24,', 'Jan 31,', 'Feb 2,', 'Feb 5,', 'Feb 6,', 'Feb 7,', 'Feb 11,', 'Feb 12,', 'Feb 14,', 'Feb 15,', 'Feb 18,', 'Feb 19,', 'Feb 20,', 'Feb 21,', 'Feb 24,', 'Feb 27,', 'Feb 28,', 'Mar 5,', 'Mar 6,', 'Mar 7,', 'Mar 13,', 'Mar 14,', 'Mar 21,', 'Mar 24,', 'Mar 26,', 'Apr 3,', 'Apr 4,', 'Apr 7,', 'Apr 9,', 'Apr 10,', 'Apr 13,', 'Apr 21,', 'Apr 22,', 'Apr 24,', 'May 18,']

dates_stripped_chars = ['Dec 19', 'Dec 26', 'Dec 27', 'Dec 28', 'Dec 31', 'Jan 5', 'Jan 9', 'Jan 10', 'Jan 13', 'Jan 15', 'Jan 17', 'Jan 21', 'Jan 22', 'Jan 23', 'Jan 24', 'Jan 31', 'Feb 2', 'Feb 5', 'Feb 6', 'Feb 7', 'Feb 11', 'Feb 12', 'Feb 14', 'Feb 15', 'Feb 18', 'Feb 19', 'Feb 20', 'Feb 21', 'Feb 24', 'Feb 27', 'Feb 28', 'Mar 5', 'Mar 6', 'Mar 7', 'Mar 13', 'Mar 14', 'Mar 21', 'Mar 24', 'Mar 26', 'Apr 3', 'Apr 4', 'Apr 7', 'Apr 9', 'Apr 10', 'Apr 13', 'Apr 21', 'Apr 22', 'Apr 24', 'May 18']

dates_format_month = ['December 19', 'December 26', 'December 27', 'December 28', 'December 31', 'January 5', 'January 9', 'January 10', 'January 13', 'January 15', 'January 17', 'January 21', 'January 22', 'January 23', 'January 24', 'January 31', 'February 2', 'February 5', 'February 6', 'February 7', 'February 11', 'February 12', 'February 14', 'February 15', 'February 18', 'February 19', 'February 20', 'February 21', 'February 24', 'February 27', 'February 28', 'March 5', 'March 6', 'March 7', 'March 13', 'March 14', 'March 21', 'March 24', 'March 26', 'April 3', 'April 4', 'April 7', 'April 9', 'April 10', 'April 13', 'April 21', 'April 22', 'April 24', 'May 18']

dates_format_year = ['December 19 2014', 'December 26 2014', 'December 27 2014', 'December 28 2014', 'December 31 2014', 'January 5 2015', 'January 9 2015', 'January 10 2015', 'January 13 2015', 'January 15 2015', 'January 17 2015', 'January 21 2015', 'January 22 2015', 'January 23 2015', 'January 24 2015', 'January 31 2015', 'February 2 2015', 'February 5 2015', 'February 6 2015', 'February 7 2015', 'February 11 2015', 'February 12 2015', 'February 14 2015', 'February 15 2015', 'February 18 2015', 'February 19 2015', 'February 20 2015', 'February 21 2015', 'February 24 2015', 'February 27 2015', 'February 28 2015', 'March 5 2015', 'March 6 2015', 'March 7 2015', 'March 13 2015', 'March 14 2015', 'March 21 2015', 'March 24 2015', 'March 26 2015', 'April 3 2015', 'April 4 2015', 'April 7 2015', 'April 9 2015', 'April 10 2015', 'April 13 2015', 'April 21 2015', 'April 22 2015', 'April 24 2015', 'May 18 2015']

dates_datetime = [datetime.datetime(2014, 12, 19, 0, 0), datetime.datetime(2014, 12, 26, 0, 0), datetime.datetime(2014, 12, 27, 0, 0), datetime.datetime(2014, 12, 28, 0, 0), datetime.datetime(2014, 12, 31, 0, 0), datetime.datetime(2015, 1, 5, 0, 0), datetime.datetime(2015, 1, 9, 0, 0), datetime.datetime(2015, 1, 10, 0, 0), datetime.datetime(2015, 1, 13, 0, 0), datetime.datetime(2015, 1, 15, 0, 0), datetime.datetime(2015, 1, 17, 0, 0), datetime.datetime(2015, 1, 21, 0, 0), datetime.datetime(2015, 1, 22, 0, 0), datetime.datetime(2015, 1, 23, 0, 0), datetime.datetime(2015, 1, 24, 0, 0), datetime.datetime(2015, 1, 31, 0, 0), datetime.datetime(2015, 2, 2, 0, 0), datetime.datetime(2015, 2, 5, 0, 0), datetime.datetime(2015, 2, 6, 0, 0), datetime.datetime(2015, 2, 7, 0, 0), datetime.datetime(2015, 2, 11, 0, 0), datetime.datetime(2015, 2, 12, 0, 0), datetime.datetime(2015, 2, 14, 0, 0), datetime.datetime(2015, 2, 15, 0, 0), datetime.datetime(2015, 2, 18, 0, 0), datetime.datetime(2015, 2, 19, 0, 0), datetime.datetime(2015, 2, 20, 0, 0), datetime.datetime(2015, 2, 21, 0, 0), datetime.datetime(2015, 2, 24, 0, 0), datetime.datetime(2015, 2, 27, 0, 0), datetime.datetime(2015, 2, 28, 0, 0), datetime.datetime(2015, 3, 5, 0, 0), datetime.datetime(2015, 3, 6, 0, 0), datetime.datetime(2015, 3, 7, 0, 0), datetime.datetime(2015, 3, 13, 0, 0), datetime.datetime(2015, 3, 14, 0, 0), datetime.datetime(2015, 3, 21, 0, 0), datetime.datetime(2015, 3, 24, 0, 0), datetime.datetime(2015, 3, 26, 0, 0), datetime.datetime(2015, 4, 3, 0, 0), datetime.datetime(2015, 4, 4, 0, 0), datetime.datetime(2015, 4, 7, 0, 0), datetime.datetime(2015, 4, 9, 0, 0), datetime.datetime(2015, 4, 10, 0, 0), datetime.datetime(2015, 4, 13, 0, 0), datetime.datetime(2015, 4, 21, 0, 0), datetime.datetime(2015, 4, 22, 0, 0), datetime.datetime(2015, 4, 24, 0, 0), datetime.datetime(2015, 5, 18, 0, 0)]

ticket_links_raw = ['\n\t\t\n\t\t<a href="http://www.axs.com/events/254326/nathaniel-rateliff-nathaniel-rateliff-and-the-night-sweats-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/253769/boombox-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/253770/boombox-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/254368/trombone-shorty-orleans-avenue-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/253771/boombox-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256326/g-eazy-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255645/mac-miller-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/254000/who-s-bad-the-world-s-1-michael-jackson-tribute-band-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256703/colorado-up-the-inaugural-concert-tickets?skin=ogden" title="Sold Out" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_7"><i class="fa fa-ticket fa-secondary"></i>Sold Out</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255770/reel-big-fish-less-than-jake-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255180/guster-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255217/cold-war-kids-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/254001/railroad-earth-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/254003/railroad-earth-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/254004/railroad-earth-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255218/the-floozies-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256133/logic-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256272/bush-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256030/moe-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256031/moe-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255825/borgore-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255237/sleaterykinney-tickets?skin=ogden" title="Sold Out" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_7"><i class="fa fa-ticket fa-secondary"></i>Sold Out</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256760/joe-russo-s-almost-dead-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256761/joe-russo-s-almost-dead-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/254372/hozier-tickets?skin=ogden" title="Sold Out" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_7"><i class="fa fa-ticket fa-secondary"></i>Sold Out</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255324/dr-dog-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/254373/galactic-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/254374/galactic-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256444/gov-t-mule-with-special-guest-john-scofield-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255896/iration-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255231/the-new-deal-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256878/gregory-alan-isakov-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256103/datsik-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256104/datsik-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256781/twiddle-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256436/mat-kearney-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255920/sam-hunt-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256638/the-gaslight-anthem-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256711/tv-on-the-radio-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256362/dan-shay-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256639/the-sing-off-live-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256139/punch-brothers-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255813/father-john-misty-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/256668/north-mississippi-allstars-anders-osborne-present-n-m-o-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/254784/sixx-a-m-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/254239/nightwish-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255181/milky-chance-tickets?skin=ogden" title="Sold Out" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_7"><i class="fa fa-ticket fa-secondary"></i>Sold Out</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/255704/ok-go-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t', '\n\t\t\n\t\t<a href="http://www.axs.com/events/254240/kamelot-tickets?skin=ogden" title="Buy Tickets" target="_blank" class="btn-tickets accentBackground widgetBorderColor secondaryColor tickets status_1"><i class="fa fa-ticket fa-secondary"></i>Buy Tickets</a>\n\t']

ticket_links = ['http://www.axs.com/events/254326/nathaniel-rateliff-nathaniel-rateliff-and-the-night-sweats-tickets?skin=ogden', 'http://www.axs.com/events/253769/boombox-tickets?skin=ogden', 'http://www.axs.com/events/253770/boombox-tickets?skin=ogden', 'http://www.axs.com/events/254368/trombone-shorty-orleans-avenue-tickets?skin=ogden', 'http://www.axs.com/events/253771/boombox-tickets?skin=ogden', 'http://www.axs.com/events/256326/g-eazy-tickets?skin=ogden', 'http://www.axs.com/events/255645/mac-miller-tickets?skin=ogden', 'http://www.axs.com/events/254000/who-s-bad-the-world-s-1-michael-jackson-tribute-band-tickets?skin=ogden', 'http://www.axs.com/events/256703/colorado-up-the-inaugural-concert-tickets?skin=ogden', 'http://www.axs.com/events/255770/reel-big-fish-less-than-jake-tickets?skin=ogden', 'http://www.axs.com/events/255180/guster-tickets?skin=ogden', 'http://www.axs.com/events/255217/cold-war-kids-tickets?skin=ogden', 'http://www.axs.com/events/254001/railroad-earth-tickets?skin=ogden', 'http://www.axs.com/events/254003/railroad-earth-tickets?skin=ogden', 'http://www.axs.com/events/254004/railroad-earth-tickets?skin=ogden', 'http://www.axs.com/events/255218/the-floozies-tickets?skin=ogden', 'http://www.axs.com/events/256133/logic-tickets?skin=ogden', 'http://www.axs.com/events/256272/bush-tickets?skin=ogden', 'http://www.axs.com/events/256030/moe-tickets?skin=ogden', 'http://www.axs.com/events/256031/moe-tickets?skin=ogden', 'http://www.axs.com/events/255825/borgore-tickets?skin=ogden', 'http://www.axs.com/events/255237/sleaterykinney-tickets?skin=ogden', 'http://www.axs.com/events/256760/joe-russo-s-almost-dead-tickets?skin=ogden', 'http://www.axs.com/events/256761/joe-russo-s-almost-dead-tickets?skin=ogden', 'http://www.axs.com/events/254372/hozier-tickets?skin=ogden', 'http://www.axs.com/events/255324/dr-dog-tickets?skin=ogden', 'http://www.axs.com/events/254373/galactic-tickets?skin=ogden', 'http://www.axs.com/events/254374/galactic-tickets?skin=ogden', 'http://www.axs.com/events/256444/gov-t-mule-with-special-guest-john-scofield-tickets?skin=ogden', 'http://www.axs.com/events/255896/iration-tickets?skin=ogden', 'http://www.axs.com/events/255231/the-new-deal-tickets?skin=ogden', 'http://www.axs.com/events/256878/gregory-alan-isakov-tickets?skin=ogden', 'http://www.axs.com/events/256103/datsik-tickets?skin=ogden', 'http://www.axs.com/events/256104/datsik-tickets?skin=ogden', 'http://www.axs.com/events/256781/twiddle-tickets?skin=ogden', 'http://www.axs.com/events/256436/mat-kearney-tickets?skin=ogden', 'http://www.axs.com/events/255920/sam-hunt-tickets?skin=ogden', 'http://www.axs.com/events/256638/the-gaslight-anthem-tickets?skin=ogden', 'http://www.axs.com/events/256711/tv-on-the-radio-tickets?skin=ogden', 'http://www.axs.com/events/256362/dan-shay-tickets?skin=ogden', 'http://www.axs.com/events/256639/the-sing-off-live-tickets?skin=ogden', 'http://www.axs.com/events/256139/punch-brothers-tickets?skin=ogden', 'http://www.axs.com/events/255813/father-john-misty-tickets?skin=ogden', 'http://www.axs.com/events/256668/north-mississippi-allstars-anders-osborne-present-n-m-o-tickets?skin=ogden', 'http://www.axs.com/events/254784/sixx-a-m-tickets?skin=ogden', 'http://www.axs.com/events/254239/nightwish-tickets?skin=ogden', 'http://www.axs.com/events/255181/milky-chance-tickets?skin=ogden', 'http://www.axs.com/events/255704/ok-go-tickets?skin=ogden', 'http://www.axs.com/events/254240/kamelot-tickets?skin=ogden']