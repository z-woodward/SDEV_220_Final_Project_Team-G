''' 
@Program: generate
@Author: Donald Osgood
@Last Date: 2023-11-23 14:35:00
@Purpose:Donald Osgood
'''
import json
from flask import Blueprint, request
from engines import name_generator

apis_generator_blueprint = Blueprint("generators_api", "generator", url_prefix="/api")

@apis_generator_blueprint.route("/generate_name", methods=["POST"])
def generate_name():
    generator = name_generator.RestaurantNameGenerator()
    json_data=request.json    
    genre = json_data["genre"]
    language = json_data["language"]
    word_type = json_data["word_type"]
    tone = json_data["tone"]
    style = json_data["style"]
    selected_font = json_data["font"]
    
    if not all([genre, language, word_type, tone, style]):
        result = "Error: All selections must be made."
    else:
        name = generator.generate_name(genre, language, word_type, tone, style)
        result = {'results':name}
        return json.dumps(result)