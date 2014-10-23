import models
from app import db

db.engine.execute("DROP TABLE all_venues")

db.create_all()

def create_denver_venues():
	gothic = models.Venue(venueName = "Gothic Theatre", street = "3263 S Broadway", city = "Englewood", state = "CO", website = "http://www.gothictheatre.com/events")
	bluebird = models.Venue(venueName = "Bluebird Theater", street = "3317 E Colfax Ave", city = "Denver", state = "CO", website = "http://www.bluebirdtheater.net/events")
	ogden = models.Venue(venueName = "Ogden Theatre", street = "935 E Colfax Ave", city = "Denver", state = "CO", website = "http://www.ogdentheatre.com/events")
	fillmore = models.Venue(venueName = "Fillmore Auditorium", street = "1510 Clarkson St", city = "Denver", state = "CO", website = "http://www.fillmoreauditorium.org/events/")
	firstbank = models.Venue(venueName = "1ST BANK", street = "11450 Broomfield Lane", city = "Broomfield", state = "CO", website = "http://www.1stbankcenter.com/events")
	fiddlers_green = models.Venue(venueName = "Fiddler's Green Amphitheatre", street = "6350 Greenwood Plaza Blvd", city = "Englewood", state = "CO", website = "http://www.fiddlersgreenamp.com/events")
	paramount = models.Venue(venueName = "Paramount Theatre", street = "1621 Glenarm Pl", city = "Denver", state = "CO", website = "http://www.paramountdenver.com")
	pepsi_center = models.Venue(venueName = "Pepsi Center", street = "1000 Chopper Cir", city = "Denver", state = "CO", website = "http://www.pepsicenter.com/")
	red_rocks = models.Venue(venueName = "Red Rocks Amphitheatre", street = "18300 West Alameda Parkway", city = "Morrison", state = "CO", website = "http://redrocksonline.com/")
	fox = models.Venue(venueName = "Fox Theater", street = "1135 13th St", city = "Boulder", state = "CO", website = "http://foxtheatre.com/")
	db.session.add(gothic)
	db.session.add(bluebird)
	db.session.add(ogden)
	db.session.add(fillmore)
	db.session.add(firstbank)
	db.session.add(fiddlers_green)
	db.session.add(paramount)
	db.session.add(pepsi_center)
	db.session.add(red_rocks)
	db.session.add(fox)
	db.session.commit()

create_denver_venues()
