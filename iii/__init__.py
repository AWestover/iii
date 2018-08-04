# main app

import os

from flask import Flask, render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/index')
    @app.route('/')
    def index():
        print('INDEX')
        return render_template('index.html')

    @app.route('/signin', methods=('GET', 'POST'))
    def login():
        print('asdfasdfasdf')
        return render_template('signin.html')

    @app.route('/signup')
    def signup():
        return render_template('signup.html')

    @app.route('/main')
    def main():
        return render_template('main.html')

    return app
