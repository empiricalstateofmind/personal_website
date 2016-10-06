from flask import Flask, render_template, url_for

#from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config.from_object('config.BaseConfig')

#db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

@app.route("/site-map/")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint)
            links.append((url, rule.endpoint))
    return '\n'.join([','.join(link) for link in links])


# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_home.controllers import mod_home as home_module

# Register blueprint(s)
app.register_blueprint(home_module, url_prefix='/')

# Build the database:
# This will create the database file using SQLAlchemy
#db.create_all()