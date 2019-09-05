from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, Response, \
                  stream_with_context, config
import json

mod_home = Blueprint('home', __name__, static_folder='static')

@mod_home.context_processor
def inject_dict_for_all_templates():
    return dict(project_list={'Mapping the Top 100 Climbs':'/projects/top-climbs.html',
                              'Sketches & Colourings':'/projects/sketches.html'})

@mod_home.route('/')
def index():
    return render_template('/home/index.html')

@mod_home.route('vitae/')
def vitae():
    with mod_home.open_resource('static/vitae.json') as w:
         data = json.load(w)
        
    publications = data['publications']
    conferences = data['conferences']
    reviewing = data['reviewing']
    teaching = data['teaching']

    return render_template('/home/vitae.html', publications=publications, 
                                               conferences=conferences,
                                               reviewing=reviewing,
                                               teaching=teaching)    
    
@mod_home.route('research/')
def research():
    with mod_home.open_resource('static/research.json') as w:
        data = json.load(w)
    
    topics = data['topics']

    return render_template('/home/research.html', topics=topics)

@mod_home.route('data/')
def data():

    return render_template('/home/data.html', topics=topics)      

@mod_home.route('projects/<project_slug>.html')
def projects(project_slug):
    if project_slug is None:
        return render_template('/home/projects/projects.html')
    else:
        with mod_home.open_resource('static/projects.json') as w:
            data = json.load(w)
        return render_template('/home/projects/{}.html'.format(project_slug), data=data)
    
@mod_home.route('test/')
def test():
    return render_template('/home/test.html')   
    
    