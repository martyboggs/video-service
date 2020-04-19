import sys
from flask import Flask, url_for, render_template, request, redirect
from markupsafe import escape
import os, json, boto3

app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/save-video', methods=['POST'])
def save_video():
	return 'yes'

# # Create MediaConvert client
# mediaconvert_client = boto3.client('mediaconvert', endpoint_url='https://abcd1234.mediaconvert.us-west-2.amazonaws.com')

# # Load job.json from disk and store as Python object: job_object
# with open("job.json", "r") as jsonfile:
#     job_object = json.load(jsonfile)

# # Create MediaConvert job by unpacking the arguments from job_object. The job object contains the required parameters 
# # for create_job. Pass these to create_job using Python's ** argument unpacking syntax.
# mediaconvert_client.create_job(**job_object)

# https://devcenter.heroku.com/articles/s3-upload-python
@app.route("/account/")
def account():
    return render_template('account.html')

@app.route('/sign_s3/')
def sign_s3():
	S3_BUCKET = os.environ.get('S3_BUCKET')

	file_name = request.args.get('file_name')
	file_type = request.args.get('file_type')

	s3 = boto3.client('s3')

	presigned_post = s3.generate_presigned_post(
		Bucket = S3_BUCKET,
		Key = file_name,
		Fields = {"acl": "public-read", "Content-Type": file_type},
		Conditions = [
			{"acl": "public-read"},
			{"Content-Type": file_type}
		],
		ExpiresIn = 3600
	)

	return json.dumps({
		'data': presigned_post,
		'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, file_name)
	})

@app.route("/submit_form/", methods = ["POST"])
def submit_form():
	username = request.form["username"]
	full_name = request.form["full-name"]
	avatar_url = request.form["avatar-url"]

	update_account(username, full_name, avatar_url)

	return redirect(url_for('profile'))

def update_account(username, full_name, avatar_url):
	return

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
