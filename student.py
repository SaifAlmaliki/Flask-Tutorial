from flask import Flask
from flask import render_template    # to use HTML templete
from flask import redirect, url_for  # to redirect route
from flask import request            # to POST request
app = Flask(__name__)

@app.route("/")
def student():
    return  render_template('student.html')

# http://127.0.0.1:5000/result
@app.route("/result", methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        res = request.form
        return render_template('score.html', score = res)

#-------------------------------------------------------------------------

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
    