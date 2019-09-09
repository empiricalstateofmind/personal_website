# Run a test server.
import sys
from app import app
from flask_frozen import Freezer

freezer = Freezer(app)

@freezer.register_generator
def project_urls():
    for project in ['top-climbs','projects', 'sketches']:
        yield 'home.projects', {'project_slug': project}

@freezer.register_generator
def data_urls():
    for data in ['ah-enron','ah-overflow-stack', 'ah-overflow-math','ah-movielens','ah-scopus-multilayer','ah-twitter']:
        yield 'home.data', {'data_slug': data}

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=8080, debug=True)