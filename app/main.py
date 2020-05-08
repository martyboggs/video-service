
import sys
import os
from flask import render_template

# adding this part so we always do absolute import
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from app.routes import app


@app.route('/')
def hello_world():
	return render_template('index.html')

# @app.route("/")
# def hello():
#   version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
#   message = "Hello World from Flask in a uWSGI Nginx Docker container with Python {} (default)".format(
#     version
#   )
#   return message


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=80)



