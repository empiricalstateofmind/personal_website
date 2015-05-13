from flask import Flask, render_template, Response

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config.from_object('config.BaseConfig')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_home.controllers import mod_home as home_module

# Register blueprint(s)
app.register_blueprint(home_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()