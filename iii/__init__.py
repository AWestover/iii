# main app

from os.path import join
import os

from flask import Blueprint, Flask, redirect, render_template, request, session, url_for, jsonify
import matplotlib.pyplot as plt
import numpy as np
import datetime

from . import db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    @app.route('/index')
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/signin')
    def signin():
        return render_template('signin.html')

    @app.route('/signup', methods=("POST", "GET"))
    def signup():
        if request.method == "GET":
            return render_template('signup.html')
        elif request.method == "POST":
            if db.insertUser(request.form['uname'], request.form['pwd']):
                return redirect(url_for('signin'))
            else:
                return redirect(url_for('signup', signup='fail'))

    @app.route('/main', methods=("POST",))
    def main():
        if db.verifyUser(request.form['uname'], request.form['pwd']):
            return render_template('main.html')
        else:
            return redirect(url_for('signin', signin='fail'))

    @app.route('/new-group')
    def newgroup():
        return render_template('new-group.html')
    
    @app.route('/insertAnnoyance', methods=("GET",))
    def insertAnnoyance():
        db.insertAnnoyance(request.args)
        return ""
    
    @app.route('/getAnnoyances', methods=("GET",))
    def getAnnoyances():
        ts = np.linspace(0,100,100)
        xs = (ts/3)**2+np.random.random(ts.shape)*1000
        plt.plot(ts, xs)
        newPic = "img/fig_{}.png".format(str(datetime.datetime.now()))
        for f in os.listdir('iii/static/img'):
            if 'fig' in f:
                cf = join('iii/static/img', f)
                os.remove(cf)
        plt.savefig(join("iii/static", newPic))
        plt.cla()
        
        return jsonify({
                "annoyances": db.selectAnnoyances(request.args["thegroup"]), 
                "picture": newPic
            })

    @app.route('/database', methods=("GET",))
    def database():
        return render_template("database.html", database=db.selectAllUsers())

    return app
