# upload file

from flask import Flask
from flask import render_template    # to use HTML templete
from werkzeug.utils import secure_filename # to upload file
from flask import request            # to POST request
app = Flask(__name__)

# http://127.0.0.1:5000/upload
@app.route("/upload")
def upload_file():
    return  render_template('upload.html')

# http://127.0.0.1:5000/uploader
@app.route("/uploader", methods = ['POST', 'GET'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'succussflly uploaded to directory'

#-------------------------------------------------------------------------

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
    