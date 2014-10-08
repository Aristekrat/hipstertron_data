from app import app
from models import Denver_Concerts, Venue

@app.route('/')
def default():
    return "You've reached Hipster Tron's data server. Unfortunately, there's nothing for people to do here, just scripts. Sowwy :-("

#This logic stuff should be seperated out. 
concerts = Denver_Concerts.query.order_by(Denver_Concerts.showDate)

def prep_concert_response(results):
	response = []
	for result in results:
		t = Venue.query.get(result.concertVenueId)
		bah = str(result.showDate)
		x = {"date": bah, "band": result.band, "venue": t.venueName}
		response.append(x)
	return response

response = prep_concert_response(concerts)

@app.route('/getConcerts', methods=['GET', 'OPTIONS'])
def returnConcerts():
	return jsonify(concertListings=response)

@app.route('/sendEmail', methods=['POST'])
def sendEmail():