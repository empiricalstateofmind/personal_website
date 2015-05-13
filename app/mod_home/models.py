# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class Publications(Base):

    __tablename__ = 'publications'

    title = db.Column(db.String(128),  nullable=False)
    authors = db.Column(db.String(128),  nullable=False)
    date = db.Column(db.String(128),  nullable=False)
    abstract = db.Column(db.String(1000),  nullable=False)
    image = db.Column(db.String(128),  nullable=False)
    link = db.Column(db.String(128),  nullable=True)
    arxiv = db.Column(db.String(128),  nullable=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return None

    def __repr__(self):
        return '<Publication %r>' % (self.title)  
        
class Conferences(Base):

    __tablename__ = 'conferences'

    title = db.Column(db.String(128),  nullable=False)
    location = db.Column(db.String(128),  nullable=False)
    date = db.Column(db.String(128),  nullable=False)
    abstract = db.Column(db.String(1000),  nullable=False)
    image = db.Column(db.String(128),  nullable=False)
    link = db.Column(db.String(128),  nullable=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return None

    def __repr__(self):
        return '<Conference %r>' % (self.title)  