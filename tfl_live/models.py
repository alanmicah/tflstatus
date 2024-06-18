"""
models.py created by Alan D 11/07/2022
"""

from extensions import db

class LineStatus(db.Model):
  """Line Status"""
  __tablename__='line_status'
  id = db.Column(db.VARCHAR, primary_key=True)
  name = db.Column(db.Text)
  modeName = db.Column(db.Text)
  disruptions = db.Column(db.Text)
  created = db.Column(db.TIMESTAMP)
  modified = db.Column(db.TIMESTAMP)
  lineStatuses = db.Column(db.Object)
  routeSections = db.Column(db.Float)
  serviceTypes = db.Column(db.Float)
  crowding = db.Column(db.Date)
  lastupdate = db.Column(db.TIMESTAMP)

class Disruptions(db.Model):
  """Line Disruptions"""
  __tablename__='line_disruptions'
  id = db.Column(db.Text, nullable=False, primary_key=True)
  type = db.Column(db.Text)
  restoretime = db.Column(db.Text)
  information = db.Column(db.Text)
  starttime = db.Column(db.Text)
  reports = db.Column(db.Integer)
  lastupdate = db.Column(db.TIMESTAMP)