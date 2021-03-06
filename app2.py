import os
import re
from datetime import datetime
from unicodedata import name

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

navigation = [
    {"href": "/", "caption": "Start"},
    {"href": "/hello", "caption": "Hello"},
    {"href": "/home", "caption": "Home"}
]


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
    return redirect(url_for('success_page', name=user))


@app.route("/success/<name>")
def success_page(name):
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


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    # app.run(threaded=True, port=5000)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
