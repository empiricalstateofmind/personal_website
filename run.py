# Run a test server.
import sys
from app import app
from flask_frozen import Freezer

freezer = Freezer(app)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=8080, debug=True)