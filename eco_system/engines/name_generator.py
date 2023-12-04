''' 
@Program: name_generator
@Author: Donald Osgood
@Last Date: 2023-11-22 23:09:13
@Purpose:Donald Osgood
'''
import random
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