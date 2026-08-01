COOKING_KEYWORDS = {
    "recipe", "cook", "cooking", "food", "meal",
    "ingredient", "ingredients",
    "vegetable", "vegetables",
    "fruit", "fruits",
    "chicken", "mutton", "fish", "egg",
    "rice", "biryani", "pizza", "pasta",
    "cake", "dessert", "soup", "salad",
    "breakfast", "lunch", "dinner",
    "snack", "nutrition", "calories",
    "protein", "vitamin",
    "boil", "fry", "bake", "grill",
    "steam", "roast",
    "oil", "salt", "pepper", "masala"
}

def is_cooking_query(query):
    query = query.lower().strip()
    return any(keyword in query for keyword in COOKING_KEYWORDS)