spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# Takes list of speicy_foods
# returns list of strings with the names of each spicy food
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# returns foods with heat_level >5
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"]>5]

# returns all foods formatted with pepper emojis for heat_level
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_peppers= "🌶"*food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_peppers}")
        # print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level']}")

# Takes list of spicy_foods and a string representing a cuisine
# returns a single dictionary for the spicy food whose cuise matches the cuisine being passed in
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))


def get_average_heat_level(spicy_foods):
    heat_list = [(food['heat_level']) for food in spicy_foods]
    return sum(heat_list) / (len(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

