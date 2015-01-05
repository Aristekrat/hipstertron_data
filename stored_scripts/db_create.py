import sys
sys.path.append("..")

from config import SQLALCHEMY_DATABASE_URI
from app import db
db.create_all()