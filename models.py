from extensions import db

class LineStatus(db.Model):
  """Line Status"""
  __tablename__='line_status'
  id = db.Column(db.VARCHAR, primary_key=True)
  type = db.Column(db.VARCHAR)
  name = db.Column(db.Text)
  modename = db.Column(db.Text)
  disruptions = db.Column(db.Text)
  created = db.Column(db.TIMESTAMP)
  modified = db.Column(db.TIMESTAMP)
  linestatuses = db.Column(db.JSON)
  routesections = db.Column(db.JSON)
  servicetypes = db.Column(db.JSON)
  crowding = db.Column(db.JSON)
  lastupdate = db.Column(db.TIMESTAMP)

class LineDisruptions(db.Model):
  """Line Disruptions"""
  __tablename__='line_disruptions'
  id = db.Column(db.VARCHAR, nullable=False, primary_key=True)
  type = db.Column(db.Text)
  category = db.Column(db.Text)
  categorydescription = db.Column(db.Text)
  description = db.Column(db.Text)
  affectedroutes = db.Column(db.JSON)
  affectedstops = db.Column(db.JSON)
  closuretext = db.Column(db.Text)
  lastupdate = db.Column(db.TIMESTAMP)

class Lines(db.Model):
  """Lines"""
  __tablename__='lines'
  id = db.Column(db.VARCHAR, nullable=False, primary_key=True)
  name = db.Column(db.Text)
  modeName = db.Column(db.Text)
  created = db.Column(db.TIMESTAMP)
  updated = db.Column(db.TIMESTAMP)