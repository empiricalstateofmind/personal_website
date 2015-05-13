from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, Response, \
                  stream_with_context

# Import the database object from the main app module
from app import db

# Import module forms
#from app.mod_lisa.forms import SimulationForm, GraphGenerateForm

# Import module models (i.e. User)
from app.mod_home.models import Publications, Conferences

from dbpopulate import populate_db

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_home = Blueprint('home', __name__, url_prefix='/home',
                        static_folder='static', static_url_path='/static')

@mod_home.route('/')
def index():
    return render_template('/home/index.html')

@mod_home.route('/vitae')
def vitae():

    publications = Publications.query.all()

    conferences = Conferences.query.all()  
    
    cv = {
        "education": [
            {
                "school": "University of Leeds",
                "date": "2013-Present",
                "info": [
                    "PhD Candidate"
                ]
            }
        ],
        "work": [
            {
                "job": "Winton Capital Management",
                "date": "01/01/01",
                "info": [
                    "Used Python and SQL to analyse financial market data.",
                    "Constructed tests to highlight possible bad data and cleaned it appropriately.",
                    "Took on extra responsibility after mentor suddenly had to leave the team.",
                    "Attended research workshops and seminars."
                ]
            },
        ],
        "tech": [
            {
                "skill": "Programming",
                "info": [
                    "Extensive use of Python for simulation and data analysis.",
                    "Experience with Java/MATLAB.",
                    "Knowledge of C++/Fortran.",
                    "Experience with version control and collaborative projects."
                ]
            }
        ],
        "extra": [
            {
                "item": "Treasurer of Trinity College Boat Club (2011-2012)",
                "info": [
                    "Budgeted and managed a cash flow of over"
                ]
            }
        ]
    }    
    
    return render_template('/home/vitae.html', publications=publications, conferences=conferences,
                           cv=cv)    
    
@mod_home.route('/research')
def research():
    return render_template('/home/research.html')   
    
@mod_home.route('/test')
def test():
    return "Test working"   
    
    