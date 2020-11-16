from flask import Flask
from flask import render_template # to use HTML templete

app = Flask(__name__)

# http://127.0.0.1:5000/exam/30
@app.route("/exam/<int:score>")
def exam(score):
    return render_template('result.html', mark = score)
    # mark: define in HTML templete


if __name__ == "__main__":
    # app.run()  
    app.run(debug=True) # After development remove debug=True
    