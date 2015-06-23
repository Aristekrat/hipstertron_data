import datetime

artists_stripped_html = ['In This Moment', 'Medeski, Martin and Wood', 'Third Eye Blind & Dashboard Confessional', 'Meghan Trainor', 'Danzig', 'Charli XCX & Bleachers', 'Rise Against, Killswitch Engage & Letlive', 'NOFX, Lagwagon & The Flatliners', 'Three Days Grace', 'Social Distortion', 'Empire of the Sun', 'Damian Marley, Stephen Marley, Morgan Heritage & Tarrus Riley', 'Nick Jonas & BeBe Rexha', 'ZZ Ward', 'Lotus']

dates_stripped_html = []

dates_stripped_ends = []

dates_format_special = []

dates_datetime = []

ticket_links_relative = ['/tickets.php?event=682109', '/tickets.php?event=674826', '/tickets.php?event=655354', '/tickets.php?event=658940', '/tickets.php?event=674209', '/tickets.php?event=676089', '/tickets.php?event=671412', '/tickets.php?event=679393', '/tickets.php?event=684121', '/tickets.php?event=676109', '/tickets.php?event=671772', '/tickets.php?event=685046', '/tickets.php?event=687448', '/tickets.php?event=688621', '/tickets.php?event=676925']

ticket_links = ['http://www.fillmoreauditorium.org/tickets.php?event=682109', 'http://www.fillmoreauditorium.org/tickets.php?event=674826', 'http://www.fillmoreauditorium.org/tickets.php?event=655354', 'http://www.fillmoreauditorium.org/tickets.php?event=658940', 'http://www.fillmoreauditorium.org/tickets.php?event=674209', 'http://www.fillmoreauditorium.org/tickets.php?event=676089', 'http://www.fillmoreauditorium.org/tickets.php?event=671412', 'http://www.fillmoreauditorium.org/tickets.php?event=679393', 'http://www.fillmoreauditorium.org/tickets.php?event=684121', 'http://www.fillmoreauditorium.org/tickets.php?event=676109', 'http://www.fillmoreauditorium.org/tickets.php?event=671772', 'http://www.fillmoreauditorium.org/tickets.php?event=685046', 'http://www.fillmoreauditorium.org/tickets.php?event=687448', 'http://www.fillmoreauditorium.org/tickets.php?event=688621', 'http://www.fillmoreauditorium.org/tickets.php?event=676925']

ticket_prices = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]