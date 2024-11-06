# Filename: app.py
import os
from flask import Flask, jsonify, redirect, url_for
from flask_dance.contrib.github import github
from oauth import github_blueprint

app = Flask(__name__)
app.secret_key = 'tHiS-iS-a-H@rD-tO-gUeSs-sTrInG'
app.register_blueprint(github_blueprint, url_prefix='/login')


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

@app.route('/login')
def login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    request = github.get('/user')
    username = request.json()["login"]
    return f"Your GitHub's username: {username}"

@app.route('/test')
def test_func():
    return jsonify(test="200 OK")

if __name__ == "__main__":
    app.run(debug=True)