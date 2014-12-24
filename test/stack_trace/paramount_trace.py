import datetime

artists_stripped_html = ['Home Free', 'Banff Mountain Film Festival', 'Spandau Ballet', 'David Sedaris', 'The Fab Four ', 'Air Supply ', 'Demetri Martin', 'Chris Hardwick', 'Spank! The Fifty Shades Parody', 'truTV Impractical Jokers the â\x80\x9cWhereâ\x80\x99s Larry?â\x80\x9d Tour, Starring the Tenderloins', 'Billy Idol', 'Dancing with the Stars: Live! Tour', 'Arlo Guthrie']

dates_stripped_html = ['Saturday, March 28, 2015 - 8:00 PM', None, 'On sale 12/17 at 10am!', 'Thursday, February 26, 2015 - 7:00PM &', 'Friday, February 27, 2015 - 7:00PM', 'Tuesday, January 27, 2015 - 8:00 PM', None, ' On sale now!', 'Monday May 11, 2015 - 7:30 PM', None, ' On sale Friday, November 21 at 10:00 AM', 'Saturday, February 28, 2015 - 7:30 PM', None, 'On sale now!', 'Friday, January 16, 2015 - 7:30 PM', None, 'On sale now!', 'Saturday, January 17, 2015 - 8:00 PM', None, ' On sale now!', 'Saturday, January 24, 2015 - 8:00 PM', None, ' On sale November 21 at 10:00 PM', 'Saturday, February 21, 2015 - 8:00 PM', None, ' On sale now!', 'March 7, 2015', None, 'On sale: Thursday, December 18 at 12:00 PM', 'Monday, February 9, 2015 - 8:00 PM', None, 'On sale now!', 'Tuesday, February 3, 2015 - 8:00 PM', None, 'On sale now!', 'Friday, April 24, 2015 - 7:00 PM', None, 'On sale now!']

dates_culled = ['March 28,', 'February 26,', 'February 27,', 'January 27,', 'May 11,', 'November 21', 'February 28,', 'January 16,', 'January 17,', 'January 24,', 'November 21', 'February 21,', 'March 7,', 'December 18', 'February 9,', 'February 3,', 'April 24,']

dates_stripped_chars = ['March 28', 'February 26', 'February 27', 'January 27', 'May 11', 'November 21', 'February 28', 'January 16', 'January 17', 'January 24', 'November 21', 'February 21', 'March 7', 'December 18', 'February 9', 'February 3', 'April 24']

dates_format_year = ['March 28 2015', 'February 26 2015', 'February 27 2015', 'January 27 2015', 'May 11 2015', 'November 21 2015', 'February 28 2015', 'January 16 2015', 'January 17 2015', 'January 24 2015', 'November 21 2015', 'February 21 2015', 'March 7 2015', 'December 18 2014', 'February 9 2015', 'February 3 2015', 'April 24 2015']

dates_datetime = [datetime.datetime(2015, 3, 28, 0, 0), datetime.datetime(2015, 2, 26, 0, 0), datetime.datetime(2015, 2, 27, 0, 0), datetime.datetime(2015, 1, 27, 0, 0), datetime.datetime(2015, 5, 11, 0, 0), datetime.datetime(2015, 11, 21, 0, 0), datetime.datetime(2015, 2, 28, 0, 0), datetime.datetime(2015, 1, 16, 0, 0), datetime.datetime(2015, 1, 17, 0, 0), datetime.datetime(2015, 1, 24, 0, 0), datetime.datetime(2015, 11, 21, 0, 0), datetime.datetime(2015, 2, 21, 0, 0), datetime.datetime(2015, 3, 7, 0, 0), None, datetime.datetime(2015, 2, 9, 0, 0), datetime.datetime(2015, 2, 3, 0, 0), datetime.datetime(2015, 4, 24, 0, 0)]

ticket_links = ['http://www.altitudetickets.com/event/home-free-3338/', 'http://www.altitudetickets.com/event-groups/banff-mountain-film-festival/', 'http://www.altitudetickets.com/event/spandau-ballet-3164/', 'http://www.altitudetickets.com/event/david-sedaris-3224/', 'http://www.altitudetickets.com/event/the-fab-four-3174/', 'http://www.altitudetickets.com/event/air-supply-3032/', 'http://www.altitudetickets.com/event/demetri-martin-the-persistence-of-jokes-3199/', 'http://www.altitudetickets.com/event/chris-hardwick-3232/', 'http://www.altitudetickets.com/event/spank-the-fifty-shades-parody-3202/', '/carousel/trutv-impractical-jokers', 'http://www.altitudetickets.com/event/billy-idol-3099/', 'http://www.altitudetickets.com/event/dancing-with-the-stars-live-3182/', 'http://www.altitudetickets.com/event/arlo-guthrie-2721/']