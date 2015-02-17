from flask import Flask, jsonify, make_response, request, current_app
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import config
import uuid
import os

app = Flask(__name__)
CORS(app, resources='/*', headers='Content-Type')
app.config.from_object(config)

db = SQLAlchemy(app)

import models

# Routes - for whatever reason the routes fail with No 'Access-Control-Allow-Origin' errors when placed outside of app.py
# This is true even of the routes logic. It's baffling.
def prep_concert_response(results):
	response = []
	for result in results:
		venue_info = models.Venue.query.get(result.concertVenueId)
		string_date = str(result.showDate) #sending in the object straight causes a cross origin error for some reason.
		concert = {"date": string_date, "band": result.band, "showLink": result.showLink, "venue": venue_info.venueName, "price": result.price}
		response.append(concert)
	return response

@app.route('/')
def default():
    return "You've reached Hipster Tron's data server. Unfortunately, there's nothing for people to do here, just scripts. Sowwy :-("

@app.route('/getConcerts/<int:result_count>/<int:offset_number>', methods=['GET', 'OPTIONS'])
def returnConcerts(result_count, offset_number):
	concerts = models.Denver_Concerts.query.order_by(models.Denver_Concerts.showDate).limit(result_count).offset(offset_number)
	response = prep_concert_response(concerts)
	return jsonify(concertListings=response)

@app.route('/sendEmail', methods=['POST'])
def sendEmail():
	email_data = request.get_json()
	user_id = str(uuid.uuid4())
	new_user = models.Users(email = email_data['email'], frequency = email_data['frequency'], userId = user_id)
	db.session.add(new_user)
	try: 
		db.session.commit()
		resp = "Complete"
	except:
		db.session.rollback()
		resp = make_response("Not Unique", 401)
	finally:
		return resp 
		db.session.close()
   
# Server Start
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 8000))
	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(port)
	IOLoop.instance().start()