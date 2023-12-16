""" 
@Program: name_generator
@Author: Donald Osgood
@Last Date: 2023-11-22 23:09:13
@Purpose:Donald Osgood
"""
import random
from engines import corpora_extension


class RestaurantNameGenerator:
    def __init__(self):
        pass
    def generate_name(self, genre, word_type, style):       
        prefixes = ["Adjective", "Noun"]
        prefix= random.choice(prefixes)
        prefix_word = ""        
        if prefix == "Adjective":
            adjectives = corpora_extension.words['adjs']
            prefix_word=  random.choice(adjectives['adjs'])
        elif prefix == "Noun":
            nouns_data = corpora_extension.words['nouns']
            prefix_word = random.choice(nouns_data['nouns'])
        
        if word_type == "One Word":
            one_word = self.get_one_word(genre,style)
            result = f"{prefix_word.capitalize()} {one_word.capitalize()}"
        elif word_type == "Multiple Words":
            num_words = random.randint(1, 2)  # Adjust the range as needed
            additional_words_list = [
                random.choice(self.get_additional_words(genre,style))
                for _ in range(num_words)
            ]  
               
            result = f"{prefix_word.capitalize()} {' '.join(additional_words_list)}"
        else:
            result = "Invalid word_type selection"

        return result

    def get_one_word(self, genre, style):
        categories = ["Adjective", "Noun", "AdditionalWord"]
        selected_category = random.choice(categories)

        if selected_category == "Adjective":
            adjectives = corpora_extension.words['adjs']
            return random.choice(adjectives['adjs'])
        elif selected_category == "Noun":
            nouns_data = corpora_extension.words['nouns']
            return random.choice(nouns_data['nouns'])
            
        elif selected_category == "AdditionalWord":
            return random.choice(self.get_additional_words(genre, style))

    def get_additional_words(self, genre, style):
        """_summary_

        Args:
            genre (_type_): string
            language (_type_): string
            style (_type_): string

        Returns:
            _type_: string
        """
        additional_words = []
        if genre == "Italian":
            data = corpora_extension.culture["italian"]
            additional_words.extend(data["italian"])
        elif genre == "Asian":
            data = corpora_extension.culture["chinese"]
            additional_words.extend(data["chinese"])
        elif genre == "Mexican":
            data = corpora_extension.culture["mexican"]
            additional_words.extend(data["mexican"])
        elif genre == "American":
            additional_words.extend(["Burger", "Diner", "Grill", "Barbecue"])
        if style == "Modern":
            additional_words.extend(["Fusion", "Express", "Hub", "Lounge"])
        elif style == "Traditional":
            additional_words.extend(["Classic", "Vintage", "Authentic", "Heritage"])
        return additional_words
