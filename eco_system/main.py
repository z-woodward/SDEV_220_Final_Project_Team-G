""" 
@Program: app
@Author: Donald Osgood
@Last Date: 2023-11-22 22:55:33
@Purpose:Donald Osgood
"""
# Flask application code

from flask import Flask
from flask_bootstrap import Bootstrap
from generators.view import view_generator_blueprint
from generators.apis import apis_generator_blueprint

app = Flask(__name__)
Bootstrap(app)
app.register_blueprint(view_generator_blueprint)
app.register_blueprint(apis_generator_blueprint)

if __name__ == "__main__":
    app.run()
