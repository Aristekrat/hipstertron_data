from config import SQLALCHEMY_DATABASE_URI
from app import db
import models

import sys
#The pathing is confused and uncoordinated between scrape.py, this file, and the site specific calls. They need to be sorted out. 
sys.path.append("scraper/")

db.engine.execute("DROP TABLE denver_concerts")

db.create_all()

exec(compile(open('scraper/scrape.py', "rb").read(), 'scrape.py', 'exec'))