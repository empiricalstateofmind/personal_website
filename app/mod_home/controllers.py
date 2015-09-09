from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, Response, \
                  stream_with_context
import json
import os

# Import the database object from the main app module
from app import db

# Import module forms
#from app.mod_lisa.forms import SimulationForm, GraphGenerateForm

# Import module models (i.e. User)
from app.mod_home.models import Publications, Conferences

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_home = Blueprint('home', __name__, url_prefix='/home',
                         static_folder='static', static_url_path='/static',)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
                         

@mod_home.route('/')
def index():
    return render_template('/home/index.html')

@mod_home.route('/vitae/')
def vitae():

    with open(os.path.join(APP_STATIC,'portfolio.json'),'r') as w:
        data = json.load(w)
        
    publications = data['publications']
    conferences = data['conferences']
    cv = data['cv']

    return render_template('/home/vitae.html', publications=publications, conferences=conferences,
                           cv=cv)    
    
#@mod_home.route('/research')
#def research():
#    return render_template('/home/research.html')   
    
@mod_home.route('/test/')
def test():
    return "Test working"   
    
    