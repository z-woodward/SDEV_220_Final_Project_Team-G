import tkinter as tk
from tkinter import ttk, font
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

class RestaurantNameGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Name Generator")

        style = ttk.Style()
        style.theme_use("clam")  # You can try different themes

        self.generator = RestaurantNameGenerator()

        # Adding padding to the outer frame
        outer_frame = ttk.Frame(self.root, padding="20")
        outer_frame.grid(row=0, column=0)

        # Genre Selection
        genre_label = ttk.Label(outer_frame, text="Select Restaurant Genre:")
        genre_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.genre_var = tk.StringVar()
        genre_options = ["Italian", "Asian", "Mexican", "American", "Other"]
        genre_dropdown = ttk.Combobox(outer_frame, textvariable=self.genre_var, values=genre_options)
        genre_dropdown.grid(row=0, column=1, padx=10, pady=5)

        # Language Selection
        language_label = ttk.Label(outer_frame, text="Select Language:")
        language_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.language_var = tk.StringVar()
        language_options = ["English", "Chinese", "Spanish", "Other"]
        language_dropdown = ttk.Combobox(outer_frame, textvariable=self.language_var, values=language_options)
        language_dropdown.grid(row=1, column=1, padx=10, pady=5)

        # Font Selection Dropdown
        font_label = ttk.Label(outer_frame, text="Select Font:")
        font_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.font_var = tk.StringVar()
        font_options = ["Arial", "Helvetica", "Times", "Courier", "Verdana", "Impact", "Comic Sans MS", "Lucida Handwriting"]
        font_dropdown = ttk.Combobox(outer_frame, textvariable=self.font_var, values=font_options)
        font_dropdown.grid(row=2, column=1, padx=10, pady=5)

        # Word Type Selection (One Word vs Multiple)
        self.word_type_var = tk.StringVar()
        word_type_label = ttk.Label(outer_frame, text="Select Word Type:")
        word_type_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        one_word_radio = ttk.Radiobutton(outer_frame, text="One Word", variable=self.word_type_var, value="One Word")
        one_word_radio.grid(row=3, column=1, padx=10, pady=5)
        multiple_words_radio = ttk.Radiobutton(outer_frame, text="Multiple Words", variable=self.word_type_var, value="Multiple Words")
        multiple_words_radio.grid(row=3, column=2, padx=10, pady=5)

        # Tone Selection (Serious vs Light Hearted)
        self.tone_var = tk.StringVar()
        tone_label = ttk.Label(outer_frame, text="Select Tone:")
        tone_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        serious_radio = ttk.Radiobutton(outer_frame, text="Serious", variable=self.tone_var, value="Serious")
        serious_radio.grid(row=4, column=1, padx=10, pady=5)
        light_hearted_radio = ttk.Radiobutton(outer_frame, text="Light Hearted", variable=self.tone_var, value="Light Hearted")
        light_hearted_radio.grid(row=4, column=2, padx=10, pady=5)

        # Style Selection (Modern vs Traditional)
        self.style_var = tk.StringVar()
        style_label = ttk.Label(outer_frame, text="Select Style:")
        style_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        modern_radio = ttk.Radiobutton(outer_frame, text="Modern", variable=self.style_var, value="Modern")
        modern_radio.grid(row=5, column=1, padx=10, pady=5)
        traditional_radio = ttk.Radiobutton(outer_frame, text="Traditional", variable=self.style_var, value="Traditional")
        traditional_radio.grid(row=5, column=2, padx=10, pady=5)

        # Submit Button
        submit_button = ttk.Button(outer_frame, text="Generate Name", command=self.generate_name)
        submit_button.grid(row=6, column=0, columnspan=3, pady=10)

        # Results Section
        self.result_label = ttk.Label(outer_frame, text="")
        self.result_label.grid(row=7, column=0, columnspan=3, pady=20)

        # Default font for the result label
        self.result_font = font.Font(family="Arial", size=12)

    def generate_name(self):
        genre = self.genre_var.get()
        language = self.language_var.get()
        word_type = self.word_type_var.get()
        tone = self.tone_var.get()
        style = self.style_var.get()

        if not all([genre, language, word_type, tone, style]):
            self.result_label.config(text="Error: All selections must be made.")
        else:
            selected_font = self.font_var.get()
            if selected_font:
                name_font = font.Font(family=selected_font, size=12)
            else:
                name_font = font.Font(family="Arial", size=12)

            name = self.generator.generate_name(genre, language, word_type, tone, style)
            self.result_label.config(text=f"Generated Name: {name}", font=name_font)

def main():
    root = tk.Tk()
    app = RestaurantNameGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

