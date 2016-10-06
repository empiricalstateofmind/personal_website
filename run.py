# Run a test server.
import sys
from app import app
from flask_frozen import Freezer

freezer = Freezer(app)

@freezer.register_generator
def project_urls():
    for project in ['top-climbs']:
        yield 'home.projects', {'project_slug': project}

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=8080, debug=True)