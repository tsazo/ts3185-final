# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route('/')
def style():
    style = """"""

def name():
    return "<div style='text-align:center;'>Hi my name is Trinity Sazo. Trin for short.</div>"

def picture():
    return ""

def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/columbia')
def about():
    return render_template('columbia.html')

#start the server
if __name__ == "__main__":
    app.run()