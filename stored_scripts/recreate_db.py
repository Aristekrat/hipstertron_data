import sys
sys.path.append("..")

from config import SQLALCHEMY_DATABASE_URI
from app import db
import models

db.engine.execute("DROP TABLE denver_concerts")
db.engine.execute("DROP TABLE emails")

db.create_all()
