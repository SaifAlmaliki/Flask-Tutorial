from flask import Flask
from flask import render_template    # to use HTML templete

app = Flask(__name__)


# http://127.0.0.1:5000/score
@app.route("/result")
def myScore():
    dict = {'phy':50, 'math':60, 'che': 80}
    return render_template('score.html', score =dict)

#-------------------------------------------------------------------------

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)