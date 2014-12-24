import unittest
import sys
sys.path.append("../scraper")
sys.path.append("..")
from utility import ticket_linksx
from test_helpers import utilityh

class TicketLinksxTestCase(unittest.TestCase):
	def setUp(self):
		self.source = open('source/bs4_dummy.html')
		self.site_html = utilityh.soup_from_source(self.source)
		self.ticket_selector = ".buyNowTicket a"

	def test_scrape_concert_links(self):
		desired_result_set = ['/tickets.php?event=583423', '/tickets.php?event=583425', '/tickets.php?event=583424', '/tickets.php?event=583876', '/tickets.php?event=597239', '/tickets.php?event=586968', '/tickets.php?event=604275']
		self.assertEqual(ticket_linksx.scrape_concert_links(self.site_html, self.ticket_selector), desired_result_set)
	
	# def test_scrape_links_from_result_set(self):

	# def test_scrape_concert_pages(self):

	def test_ticket_link_prefix(self):
		incomplete_result_set = ['/tickets.php?event=583423', '/tickets.php?event=583425', '/tickets.php?event=583424', '/tickets.php?event=583876', '/tickets.php?event=597239', '/tickets.php?event=586968', '/tickets.php?event=604275']
		desired_result_set = ['http://www.fillmoreauditorium.org/tickets.php?event=583423', 'http://www.fillmoreauditorium.org/tickets.php?event=583425', 'http://www.fillmoreauditorium.org/tickets.php?event=583424', 'http://www.fillmoreauditorium.org/tickets.php?event=583876', 'http://www.fillmoreauditorium.org/tickets.php?event=597239', 'http://www.fillmoreauditorium.org/tickets.php?event=586968', 'http://www.fillmoreauditorium.org/tickets.php?event=604275']
		self.assertEqual(ticket_linksx.ticket_link_prefix("http://www.fillmoreauditorium.org", incomplete_result_set), desired_result_set)

	def tearDown(self):
		self.source.close()

if __name__ == '__main__':
    unittest.main()