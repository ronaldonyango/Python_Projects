import random
import tkinter
from tkinter import simpledialog, messagebox

import customtkinter as tk

tk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class MealRecommender:
    def __init__(self):
        self.root = tk.CTk()
        self.root.configure(bg="green")
        self.root.withdraw()

        self.meals = {
            'basic': ['Ugali', 'Rice', 'Spaghetti', 'Chapati', 'Chips', 'Githeri', 'Pilau', 'Matoke', 'Maandazi',
                      'Samosa',
                      'Biryani', 'Fish and Chips', 'Lasagna', 'Pizza'],
            'ugali_extra': ['Beef Stew', 'Chicken Stew', 'Deep-fried Chicken', 'Matumbo', 'Minced Meat', 'Eggs',
                            'Sukuma Wiki',
                            'Cabbage', 'Terere', 'Liver Fry', 'Oxtail Stew', 'Pork Chops'],
            'rice_extra': ['Beef Stew', 'Chicken Stew', 'Deep-fried Chicken', 'Minced Meat', 'Eggs', 'Sukuma Wiki',
                           'Cabbage',
                           'French Beans', 'Ndengu', 'Kamande', 'Beans', 'Ndengu', 'Pilipili Prawns', 'Lamb Curry',
                           'Mushroom Risotto'],
            'matoke_extra': ['Beef Stew', 'Chicken Stew', 'Fried Chicken', 'Minced Meat', 'Fish Curry', 'Eggs'],
            'chapati_extra': ['Beef Stew', 'Chicken Stew', 'Ndengu', 'Kamande', 'Beans', 'Paneer Tikka',
                              'Butter Chicken',
                              'Chole Masala'],
            'githeri_extra': ['Beef Stew', 'Chicken Stew', 'Matoke', 'Chapati', 'Vegetable Biryani', 'Kebab Platter',
                              'Mixed Grill'],
            'spaghetti_extra': ['Beef Stew', 'Chicken Stew', 'Minced Meat', 'Eggs', 'Sukuma Wiki', 'Cabbage',
                                'Creamy Garlic Shrimp Pasta', 'Chicken Alfredo', 'Pasta Carbonara', 'Pesto Pasta'],
            'pilau_extra': ['Beef Stew', 'Chicken Stew', 'Mutton Curry', 'Coconut Fish Curry', 'Vegetable Pulao',
                            'Tofu Tikka Masala'],
            'maandazi_extra': ['Fried Vegetables', 'Sukuma Wiki', 'Cabbage', 'Pumpkin Leaves'],
            'samosa_extra': ['Kachumbari', 'Tamarind Chutney', 'Chicken Shawarma', 'Falafel Wrap'],
            'biryani_extra': ['Raita', 'Cucumber Salad', 'Mint Chutney'],
            'fish_and_chips_extra': ['Tartar Sauce', 'Coleslaw', 'Lemon Wedges'],
            'lasagna_extra': ['Garlic Bread', 'Caesar Salad', 'Grilled Vegetables'],
            'pizza_extra': ['Garlic Knots', 'Mixed Greens Salad', 'Buffalo Wings'],
            'meal_drinks': {
                'Ugali': ['Soda', 'Juice', 'Water', 'Buttermilk'],
                'Rice': ['Soda', 'Water', 'Lemonade', 'Iced Tea'],
                'Spaghetti': ['Juice', 'Water', 'Cola', 'Ice Coffee'],
                'Chapati': ['Soda', 'Juice', 'Coffee', 'Mint Lemonade'],
                'Chips': ['Soda', 'Water', 'Milkshake', 'Lassi'],
                'Githeri': ['Soda', 'Juice', 'Water', 'Lime Soda'],
                'Pilau': ['Soda', 'Water', 'Ice Tea', 'Mango Lassi'],
                'Matoke': ['Juice', 'Water', 'Coconut Water', 'Pineapple Smoothie'],
                'Maandazi': ['Soda', 'Coffee', 'Tea', 'Hot Chocolate'],
                'Samosa': ['Soda', 'Water', 'Iced Coffee', 'Mango Juice'],
                'Fish and Chips': ['Soda', 'Water', 'Lemonade', 'Iced Tea'],
                'Lasagna': ['Soda', 'Water', 'Cola', 'Ice Coffee'],
                'Pizza': ['Soda', 'Juice', 'Coffee', 'Mint Lemonade'],
                'Biryani': ['Soda', 'Water', 'Mango Lassi', 'Rose Milk']
            },
            'toppings': ['Kachumbari', 'Fried Vegetables', 'Guacamole', 'Sour Cream', 'Salsa', 'Cheese Sauce',
                         'Tomato Sauce'],
            'fruits': {
                'Ugali': ['Banana', 'Watermelon', 'Mango', 'Papaya', 'Pineapple', 'Orange'],
                'Rice': ['Mango', 'Pineapple', 'Apple', 'Banana', 'Orange', 'Strawberries'],
                'Spaghetti': ['Apple', 'Orange', 'Grapes', 'Kiwi', 'Peach', 'Blueberries'],
                'Chapati': ['Grapes', 'Pear', 'Apple', 'Strawberries', 'Pomegranate', 'Raspberries'],
                'Chips': ['Strawberry', 'Kiwi', 'Mango', 'Papaya', 'Watermelon', 'Pineapple'],
                'Githeri': ['Avocado', 'Papaya', 'Mango', 'Pineapple', 'Watermelon', 'Passion Fruit'],
                'Pilau': ['Plum', 'Guava', 'Mango', 'Papaya', 'Pineapple', 'Watermelon'],
                'Matoke': ['Passion Fruit', 'Lemon', 'Mango', 'Papaya', 'Pineapple', 'Banana'],
                'Maandazi': ['Cherry', 'Coconut', 'Mango', 'Papaya', 'Pineapple', 'Watermelon'],
                'Samosa': ['Peach', 'Apricot', 'Mango', 'Papaya', 'Pineapple', 'Watermelon'],
                'Fish and Chips': ['Lemon', 'Pineapple', 'Apple', 'Banana', 'Orange', 'Strawberries'],
                'Lasagna': ['Apple', 'Orange', 'Grapes', 'Kiwi', 'Peach', 'Blueberries'],
                'Pizza': ['Grapes', 'Pear', 'Apple', 'Strawberries', 'Pomegranate', 'Raspberries'],
                'Biryani': ['Lemon', 'Mango', 'Papaya', 'Pineapple', 'Orange', 'Banana']
            }
        }

        self.messages = {
            'special_occasion': ['Date night? Let\'s go!', 'I love special occasions!!!',
                                 'A special day deserves a special meal',
                                 'You didn\'t tell me it was a special day! I\'m so excited!',
                                 'Make it a memorable celebration with this meal!',
                                 'Cheers to a fantastic special occasion!'],
            'not_hungry': ['Try this light meal', 'Not hungry? Here is a good meal light on your belly',
                           'Did you know that sometimes you do not need a heavy meal?',
                           'Listen to your body and enjoy this light and refreshing meal!',
                           'Sometimes a light meal is just what you need to feel refreshed!'],
            'quick_fix': ['It is one of those lazy days right? Worry not, I have got you!',
                          'After a long day, you deserve an early rest today!',
                          'Great choice! I have just the perfect meal for you.',
                          'Enjoy a delicious and quick meal to satisfy your cravings!',
                          'This quick fix meal will save the day!'],
            'food_choices': ['Did I get it right? Check out more like this.',
                             'Perfect selection. You will enjoy this one!',
                             'You can never go wrong with this combination.',
                             'Explore similar delicious options for your next meal!',
                             'Your taste buds will thank you for this fantastic choice!'],
            'quotes': ['The only thing I like better than talking about food is eating. - John Walters',
                       'Food is our common ground, a universal experience. - James Beard',
                       'Good food is the foundation of genuine happiness. - Auguste Escoffier',
                       'Cooking is like love. It should be entered into with abandon or not at all. - Harriet Van Horne',
                       'Eating is a necessity, but cooking is an art. - Unknown']
        }

    def get_user_input(self, prompt):
        return simpledialog.askstring("User Input", prompt, parent=self.root)

    def show_message(self, message):
        tkinter.messagebox.showinfo("Meal Recommender", message, parent=self.root)

    def generate_random_message(self, message_type):
        return random.choice(self.messages[message_type])

    def generate_random_meal(self, meal_type):
        return random.choice(self.meals[meal_type])

    def generate_random_drink(self, main_meal):
        drinks = self.meals['meal_drinks'].get(main_meal, ['Water'])  # Set default drink as 'Water'
        return random.choice(drinks)

    def generate_random_fruit(self, main_meal):
        fruits = self.meals['fruits'].get(main_meal,
                                          ['No fruit available'])  # Set default fruit as 'No fruit available'
        return random.choice(fruits)

    def generate_random_quote(self):
        return random.choice(self.messages['quotes'])

    def main(self):
        user_name = self.get_user_input("What is your name?")
        prompt_special_occasion = self.get_user_input("Is it a special occasion? (yes/no)")
        prompt_hungry = self.get_user_input("Are you hungry? (yes/no)")
        prompt_quick_fix = self.get_user_input("Do you need a quick fix? (yes/no)")

        if prompt_special_occasion.lower() == "yes":
            self.show_message(self.generate_random_message('special_occasion'))
        elif prompt_hungry.lower() == "no":
            self.show_message(self.generate_random_message('not_hungry'))
        elif prompt_quick_fix.lower() == "yes":
            self.show_message(self.generate_random_message('quick_fix'))

        self.show_message(f"Hello, {user_name}! Here's a meal suggestion for you:")
        main_meal = self.generate_random_meal('basic')
        extra_meal = self.generate_random_meal(f'{main_meal.lower()}_extra')
        drink = self.generate_random_drink(main_meal)
        topping = self.generate_random_meal('toppings')
        fruit = self.generate_random_fruit(main_meal)
        meal_message = f"Meal Recommendation for {user_name}:\n\nMain Meal: {main_meal}\nExtra Meal:{extra_meal}" \
                       f"\nDrink: {drink}\nFruit: {fruit}\nTopping: {topping}"
        self.show_message(meal_message)

        self.show_message(self.generate_random_message('food_choices'))
        self.show_message(self.generate_random_quote())


if __name__ == "__main__":
    recommender = MealRecommender()
    recommender.main()
