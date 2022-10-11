from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
  __tablename__ = 'venue'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  city = db.Column(db.String(100), nullable=False)
  state = db.Column(db.String(100), nullable=False)
  address = db.Column(db.String(500), nullable=False)
  phone = db.Column(db.String(15), nullable=False)
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(500))
  genres = db.Column(db.String(255), nullable=False)
  website_link = db.Column(db.String(500))
  seeking_talent = db.Column(db.Boolean, default=False)
  seeking_description = db.Column(db.String(500))
  shows = db.relationship('Show', backref='venue', lazy=True)
  
  def __repr__(self):
    return "{} {} {}".format(self.id, self.name, self.state)
  # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
  __tablename__ = 'artist'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  city = db.Column(db.String(100), nullable=False)
  state = db.Column(db.String(100), nullable=False)
  phone = db.Column(db.String(15), nullable=False)
  genres = db.Column(db.String(255), nullable=False)
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(500))
  website_link = db.Column(db.String(500))
  seeking_venue = db.Column(db.Boolean, default=False)
  seeking_description = db.Column(db.String(500))
  shows = db.relationship('Show', backref='artist', lazy=True)

  def __repr__(self):
    return "{} {} {}".format(self.id, self.name, self.state)
    # TODO: implement any missing fields, as a database migration using Flask-Migrate


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
  __tablename__ = 'show'
  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
  start_time = db.Column(db.DateTime)
  
  def __repr__(self):
    return "{}: Artist id: {} Venue id: {} start time: {}".format(self.id, self.artist_id, self.venue_id, self.self.start_time)