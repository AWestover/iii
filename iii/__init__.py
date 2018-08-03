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

    @app.route('/')
    def index():
        print('INDEX')
        return render_template('index.html')

    @app.route('/login', methods=('GET', 'POST'))
    def login():
        print('asdfasdfasdf')
        return render_template('login.html')

    @app.route('/signup')
    def signup():
        print(request.method)
        return render_template('signup.html')

    @app.route('/main')
    def main():
        return render_template('main.html')

    return app
