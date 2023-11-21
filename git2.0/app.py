# Flask application code
from flask import Flask, render_template, request
from tkinter import ttk, font
import tkinter as tk
from PIL import Image, ImageTk
import random

app = Flask(__name__)

class RestaurantNameGenerator:
    def __init__(self):
        self.adjectives = ['Delicious', 'Savory', 'Tasty', 'Gourmet', 'Spicy', 'Exquisite', 'Mouthwatering', 'Flavorful']
        self.nouns = ['Bites', 'Cuisine', 'Grill', 'Bistro', 'Palate', 'Feast', 'Kitchen', 'Dish']
        self.additional_words = ['Eats', 'Spot', 'Place', 'House', 'Hub', 'Joint', 'Den', 'Nosh']

    def generate_name(self, genre, language, word_type, tone, style):
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)

        if word_type == "One Word":
            additional_word = self.get_one_word(genre, language, style)
            result = f"{adjective} {noun} {additional_word}"
        elif word_type == "Multiple Words":
            num_words = random.randint(2, 4)  # Adjust the range as needed
            additional_words_list = [random.choice(self.get_additional_words(genre, language, style)) for _ in range(num_words)]
            result = f"{adjective} {noun} {' '.join(additional_words_list)}"
        else:
            result = "Invalid word_type selection"

        return result

    def get_one_word(self, genre, language, style):
        categories = ["Adjective", "Noun", "AdditionalWord"]
        selected_category = random.choice(categories)

        if selected_category == "Adjective":
            return random.choice(self.adjectives)
        elif selected_category == "Noun":
            return random.choice(self.nouns)
        elif selected_category == "AdditionalWord":
            return random.choice(self.get_additional_words(genre, language, style))

    def get_additional_words(self, genre, language, style):
        additional_words = []

        if genre == "Italian":
            additional_words.extend(["Pizza", "Pasta", "Ristorante", "Trattoria"])
        elif genre == "Asian":
            additional_words.extend(["Sushi", "Wok", "Ramen", "Tempura"])
        elif genre == "Mexican":
            additional_words.extend(["Taco", "Burrito", "Salsa", "Cantina"])
        elif genre == "American":
            additional_words.extend(["Burger", "Diner", "Grill", "Barbecue"])

        if style == "Modern":
            additional_words.extend(["Fusion", "Express", "Hub", "Lounge"])
        elif style == "Traditional":
            additional_words.extend(["Classic", "Vintage", "Authentic", "Heritage"])

        return additional_words

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_name', methods=['POST'])
def generate_name():
    generator = RestaurantNameGenerator()

    genre = request.form.get('genre')
    language = request.form.get('language')
    word_type = request.form.get('word_type')
    tone = request.form.get('tone')
    style = request.form.get('style')
    selected_font = request.form.get('font')

    if not all([genre, language, word_type, tone, style]):
        result = "Error: All selections must be made."
    else:
        name = generator.generate_name(genre, language, word_type, tone, style)
        result = f"Generated Name: {name}"

    # Pass selected options back to the template
    return render_template('index.html', result=result, selected_font=selected_font, selected_genre=genre, selected_language=language, selected_word_type=word_type, selected_tone=tone, selected_style=style)

if __name__ == '__main__':
    app.run(debug=True)

