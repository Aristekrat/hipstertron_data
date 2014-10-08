from app import db

class Venue(db.Model):
	__tablename__ = "all_venues"
	__table_args__ = {'extend_existing': True}
	venueId = db.Column(db.Integer, primary_key=True)
	venueName = db.Column(db.String(100), nullable=False)
	street = db.Column(db.String(100))
	city = db.Column(db.String(64))
	state = db.Column(db.String(64))
	website = db.Column(db.String(120))

	def __repr__(self):
		return '<Venue %r>' % self.venueName

class Denver_Concerts(db.Model):
	__tablename__ = "denver_concerts"
	showId = db.Column(db.Integer, primary_key=True)
	showDate = db.Column(db.Date, nullable=False)
	band = db.Column(db.String(255), index=True, nullable=False)
	concertVenueId = db.Column(db.Integer, db.ForeignKey('all_venues.venueId'))
	concertVenue = db.relationship('Venue', backref=db.backref('concert'))

	def __repr__(self):
		return '<band %r>' % self.band

class Emails(db.Model):
	__tablename__ = "emails"
	email = db.Column(db.String(120), nullable=False, primary_key=True)

# db.create_all()