"""
Here the models for our database is defined.

I am using Postgres, Flask-SQLAlchemy for this application.

For an introduction to Flask-SQLAlchemy check out: http://flask-sqlalchemy.pocoo.org/2.1/

__init__ function for each model is a constructor, and is necessary to enter
""" 
from app import db

class HTML(db.Model):
    """
    This model stores scraped webpages
    
    parameters:
    @page - the full text of the page
    @links - json dump of the links on the page

    """
    __tablename__ = 'html'
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.String)
    links = db.Column(db.String)

    def __init__(self,page, links):
        self.page = page
        self.links = links

