from flask import Flask, jsonify, make_response, request, current_app
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import time
import calendar
import os

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
		x = {"date": temp_fix, "band": result.band, "showLink": result.showLink, "venue": t.venueName}
		response.append(x)
	return response

@app.route('/')
def default():
    return "You've reached Hipster Tron's data server. Unfortunately, there's nothing for people to do here, just scripts. Sowwy :-("

def get_last_of_month(month_int):
	month_range = calendar.monthrange(2014, month_int)
	current_day = time.strftime("%Y-%m-%d")
	current_day = current_day.split("-")
	current_day[2] = str(month_range[1])
	last_of_month = '-'.join(current_day)
	return last_of_month

def prep_concert_chunk(response, chunk_num, last_of_month):
	chunk = []
	for r in response: 
		if chunk_num == 1 and r['date'] < last_of_month:
			chunk.append(r)
		elif chunk_num == 2 and r['date'] > last_of_month:
			chunk.append(r)
	return chunk

@app.route('/getConcerts', methods=['GET', 'OPTIONS'])
def returnConcerts():
	concerts = models.Denver_Concerts.query.order_by(models.Denver_Concerts.showDate)
	response = prep_concert_response(concerts)
	last_of_month = get_last_of_month(10)
	y = prep_concert_chunk(response, 1, last_of_month)
	return jsonify(concertListings=y)

@app.route('/getConcertsTwo', methods=['GET', 'OPTIONS'])
def returnNextConcerts():
	concerts = models.Denver_Concerts.query.order_by(models.Denver_Concerts.showDate)
	response = prep_concert_response(concerts)
	last_of_month = get_last_of_month(10)
	y = prep_concert_chunk(response, 2, last_of_month)
	return jsonify(concertListings=y)

@app.route('/sendEmail', methods=['POST'])
def sendEmail():
	email_data = request.get_json()
	newEmail = models.Emails(email = email_data['email'], frequency = email_data['frequency'])
	db.session.add(newEmail)
	db.session.commit()
	return "Complete"
   
# Server Start
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 8000))
	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(port)
	IOLoop.instance().start()