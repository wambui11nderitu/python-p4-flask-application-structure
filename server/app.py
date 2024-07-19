#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome , to my page!</h1>'
@app.route('/string:username>')
def hello_user(username):
    return f'<h1>Welcome, {username}!</h1>'
