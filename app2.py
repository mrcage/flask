import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name="John Doe")
    # return "<h1>Hello World</h1>"


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
    else:
        user = request.args.get('name')
    return redirect(url_for('success', name=user))


if __name__ == '__main__':
    # app.run(threaded=True, port=5000)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
