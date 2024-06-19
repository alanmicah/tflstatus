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
  lineStatuses = db.Column(db.JSON)
  routeSections = db.Column(db.JSON)
  serviceTypes = db.Column(db.JSON)
  crowding = db.Column(db.JSON)
  lastupdate = db.Column(db.TIMESTAMP)

class LineDisruptions(db.Model):
  """Line Disruptions"""
  __tablename__='line_disruptions'
  id = db.Column(db.Text, nullable=False, primary_key=True)
  type = db.Column(db.Text)
  category = db.Column(db.Text)
  categoryDescription = db.Column(db.Text)
  description = db.Column(db.Text)
  affectedRoutes = db.Column(db.JSON)
  affectedStops = db.Column(db.JSON)
  closureText = db.Column(db.Text)
  lastupdate = db.Column(db.TIMESTAMP)