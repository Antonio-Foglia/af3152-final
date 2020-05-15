# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template, request
from F1_standings import f1

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    #return "Hello world!"
    return render_template("index.html")

@app.route("/cat")
def tenosix():
    return render_template("cat_names.html")

@app.route("/sport")
def sports():
    return render_template("sport.html")


@app.route("/F1", methods=["GET", "POST"])
def year():
    if request.method == "GET":
       return render_template("year.html")
        
    elif request.method == "POST":
        year = request.form["year"]
        f1(year)
        return render_template("F1_years/F1_{}.html".format(year))
    
    
    
    


    

#start the server
if __name__ == "__main__":
    app.run()