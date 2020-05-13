
import sys
import os
from flask import Flask, render_template
from routes.video_routes import video_api
from routes.test_routes import test_api

app = Flask(__name__)

app.register_blueprint(video_api, url_prefix='/video')
app.register_blueprint(test_api, url_prefix='/test')


@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route("/hello")
def hello():
  version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
  message = "Hello World from Flask in a uWSGI Nginx Docker container with Python {} (default)".format(
    version
  )
  return message


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=80)



