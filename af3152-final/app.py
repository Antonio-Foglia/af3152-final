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
@app.route("/")
def hello():
    #return "Hello world!"
    return render_template("index.html")

@app.route("/1006")
def tenosix():
    return render_template("tenosix.html")

#start the server
if __name__ == "__main__":
    app.run()