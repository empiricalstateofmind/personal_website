from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, Response, \
                  stream_with_context, config
import json

mod_home = Blueprint('home', __name__, static_folder='static')

@mod_home.context_processor
def inject_dict_for_all_templates():
    return dict(project_list={'Mapping the Top 100 Climbs':'/projects/top-climbs.html'})

@mod_home.route('/')
def index():
    return render_template('/home/index.html')

@mod_home.route('vitae/')
def vitae():
    with mod_home.open_resource('static/portfolio.json') as w:
         data = json.load(w)
        
    publications = data['publications']
    conferences = data['conferences']
    cv = data['cv']

    return render_template('/home/vitae.html', publications=publications, conferences=conferences,
                           cv=cv)    
    
@mod_home.route('research/')
def research():
    with mod_home.open_resource('static/research.json') as w:
        data = json.load(w)
    
    topics = data['topics']

    return render_template('/home/research.html', topics=topics)   

@mod_home.route('projects/<project_slug>.html')
def projects(project_slug):
    if project_slug is None:
        return render_template('/home/projects/projects.html')
    else:
        return render_template('/home/projects/{}.html'.format(project_slug))
    
@mod_home.route('test/')
def test():
    return render_template('/home/test.html')   
    
    