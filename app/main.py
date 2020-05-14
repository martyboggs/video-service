
import sys
import os
import boto3
from flask import Flask, render_template
from routes.video_routes import video_api
from routes.test_routes import test_api
# pylint: disable=E1101

app = Flask(__name__)

app.register_blueprint(video_api, url_prefix='/video')
app.register_blueprint(test_api, url_prefix='/test')

@app.route('/')
def index():
  s3 = boto3.resource('s3')
  # for bucket in s3.buckets.all():
  #   print(bucket.name)
  bucketName = 'video-service2'
  bucket = s3.Bucket(bucketName)
  files = bucket.objects.all()
  return render_template('index.html', data=files)

@app.route('/upload')
def hello_world():
  return render_template('upload.html')

@app.route("/hello")
def hello():
  version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
  message = "Hello World from Flask in a uWSGI Nginx Docker container with Python {} (default)".format(
    version
  )
  return message

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=80)



