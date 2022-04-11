import os
from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import re

app = Flask(__name__)

navigation = [{"href": "/", "caption": "Home"},
              {"href": "/date", "caption": "Date and time"}]


@app.route('/')
def index():
    return render_template('index.html', navigation=navigation, name="John Doe")
    # return "<h1>Hello World</h1>"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
    else:
        user = request.args.get('name')
    return redirect(url_for('hello_there', name=user))


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content


@app.route("/date")
def date():
    now = datetime.now()
    return now.strftime("%A, %d %B, %Y at %X")


if __name__ == '__main__':
    # app.run(threaded=True, port=5000)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
