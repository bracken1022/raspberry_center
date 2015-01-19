#! /usr/bin/python 
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

app.run(debug = True, host='0.0.0.0')
