# main app

import os

from flask import Flask, render_template

from . import db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/index')
    @app.route('/')
    def index():
        # print(help(db))
        return render_template('index.html')

    @app.route('/signin', methods=('GET', 'POST'))
    def login():
        return render_template('signin.html')

    @app.route('/signup')
    def signup():
        return render_template('signup.html')

    @app.route('/main')
    def main():
        return render_template('main.html')

    return app
