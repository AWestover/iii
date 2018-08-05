# main app

import os

from flask import Blueprint, Flask, redirect, render_template, request, session, url_for

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

    @app.route('/signup', methods=["POST", "GET"])
    def signup():
        if request.method == "GET":
            return render_template('signup.html')
        elif request.method == "POST":
            db.insertUser(request.form['uname'], request.form['pwd'])
            return redirect(url_for('signin'))

    @app.route('/main', methods=["POST"])
    def main():
        if db.verifyUser(request.form['uname'], request.form['pwd']):
            return render_template('main.html')
        else:
            return redirect(url_for('signin', login='fail'))

    @app.route('/annoyance', methods=["GET", "POST"])
    def annoyance():
        if request.method == "GET":
            return db.selectAnnoyances(request.args["group"])
        elif request.method == "POST":
            db.insertAnnoyance(request.args)

    @app.route('/database', methods=["GET"])
    def database():
        return render_template("database.html", database=db.selectAllUsers())

    return app
