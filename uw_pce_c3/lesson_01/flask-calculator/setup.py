# setup.py for flask-calculator

from model import db, SavedTotal

db.connect()
db.create_tables([SavedTotal])