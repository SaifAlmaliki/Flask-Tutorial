from flask import Flask
from flask import render_template    # to use HTML templete
from flask import redirect, url_for  # to redirect route

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello_admin")
def hello_admin():
    return 'Hello Admin'

# Variable Route (http://127.0.0.1:5000/welcome/SAIF)
@app.route("/welcome/<name>")
def welcome(name):
    return "Hello %s!" %name

#---------------------------------------------


# rendering Templete - passing parameters from python to HTML templete
# (http://127.0.0.1:5000/hello/SAIF)
@app.route("/hello/<user>")
def hello_user(userName):
    return render_template('index.html', name = userName)

#------------------------------------------------------------------------

# Use Building- route redicrect
# http://127.0.0.1:5000/user/admin
@app.route("/user/<name>")
def user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))  # redirect to hello_admin url
    else:
        return redirect(url_for('hello_user', userName=name))

#------------------------------------------------------------------------

@app.route("/members")
def members():
    return "Members"

#-------------------------------------------------------------------------

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
    