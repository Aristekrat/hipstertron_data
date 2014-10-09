from flask import Flask, jsonify, make_response, request, current_app
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

app = Flask(__name__)
CORS(app, resources='/*', headers='Content-Type')
app.config.from_object('config')

db = SQLAlchemy(app)

import models

#Begin Routes - for whatever reason the routes fail with No 'Access-Control-Allow-Origin' errors when placed outside of app.py
#This is true even of the routes logic. It's baffling.
def prep_concert_response(results):
	response = []
	for result in results:
		t = models.Venue.query.get(result.concertVenueId)
		temp_fix = str(result.showDate) #sending in the object straight causes a cross origin error for some damn reason.
		x = {"date": temp_fix, "band": result.band, "venue": t.venueName}
		response.append(x)
	return response

@app.route('/')
def default():
    return "You've reached Hipster Tron's data server. Unfortunately, there's nothing for people to do here, just scripts. Sowwy :-("

@app.route('/getConcerts', methods=['GET', 'OPTIONS'])
def returnConcerts():
	concerts = models.Denver_Concerts.query.order_by(models.Denver_Concerts.showDate)
	response = prep_concert_response(concerts)
	return jsonify(concertListings=response)

@app.route('/sendEmail', methods=['POST'])
def sendEmail():
	userEmail = request.get_json()
	newEmail = models.Emails(email = userEmail)
	db.session.add(newEmail)
	db.session.commit()
	return "Complete"

# Server Start
if __name__ == '__main__':
  http_server = HTTPServer(WSGIContainer(app))
  http_server.listen(8000)
  IOLoop.instance().start()