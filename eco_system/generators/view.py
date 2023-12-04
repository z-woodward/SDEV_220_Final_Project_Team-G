""" 
@Program: home
@Author: Donald Osgood
@Last Date: 2023-11-23 11:52:12
@Purpose:Donald Osgood
"""
from flask import Blueprint, render_template, url_for

view_generator_blueprint = Blueprint("generators_view", __name__,template_folder="templates",static_folder="static",static_url_path='/generator/static')

@view_generator_blueprint.route("/")
def generate():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template("index.html", getResultsEndPoint=url_for('generators_api.generate_name'))
