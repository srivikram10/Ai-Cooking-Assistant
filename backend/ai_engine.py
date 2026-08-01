from google import genai
from deep_translator import GoogleTranslator
from config import GEMINI_API_KEY

# Configure Gemini with new SDK
client = genai.Client(api_key=GEMINI_API_KEY)
MODEL_NAME = "gemini-2.0-flash"

# Detailed Fallback Recipe Library
PREBUILT_RECIPES = {
    "chicken biryani": {
        "title": "Chicken Biryani",
        "prep_time": "30 mins",
        "cook_time": "45 mins",
        "servings": "4",
        "ingredients": [
            "500g chicken (bone-in pieces)",
            "2 cups basmati rice (soaked 30 mins)",
            "2 large onions (thinly sliced)",
            "1 cup yogurt",
            "2 tomatoes (chopped)",
            "1 tbsp ginger-garlic paste",
            "1 tsp turmeric powder",
            "1 tsp red chili powder",
            "1 tsp biryani masala",
            "4 green cardamom pods",
            "4 cloves",
            "2 bay leaves",
            "1 cinnamon stick",
            "Fresh mint & coriander leaves",
            "4 tbsp ghee or oil",
            "Saffron strands soaked in warm milk",
            "Salt to taste"
        ],
        "steps": [
            "Wash and soak basmati rice in water for 30 minutes, then drain.",
            "Heat ghee in a heavy-bottomed pot. Add bay leaves, cardamom, cloves, and cinnamon. Sauté for 30 seconds until fragrant.",
            "Add sliced onions and fry on medium heat until deep golden brown (about 12-15 minutes). Remove half for garnish.",
            "Add ginger-garlic paste and sauté for 2 minutes until the raw smell disappears.",
            "Add chicken pieces, turmeric, red chili powder, and salt. Cook on high heat for 5 minutes, stirring well.",
            "Add chopped tomatoes and yogurt. Mix well, cover, and cook for 15 minutes until chicken is 80% done.",
            "Meanwhile, boil water with salt and whole spices. Parboil the soaked rice until 70% cooked (al dente). Drain.",
            "Layer the parboiled rice over the chicken. Sprinkle biryani masala, saffron milk, fried onions, and fresh mint/coriander.",
            "Seal the pot with aluminum foil and a tight lid. Cook on high heat for 3 minutes, then reduce to the lowest heat for 25 minutes (dum).",
            "Turn off heat and let it rest for 5 minutes. Gently mix layers before serving."
        ],
        "nutrition": {"calories": "550 kcal", "protein": "35g", "carbs": "55g", "fat": "18g", "fiber": "3g"},
        "tips": [
            "Use bone-in chicken for more flavor.",
            "Don't skip the dum (slow steam) — it's what makes biryani special.",
            "Soak the rice well to get long, separate grains."
        ]
    },
    "butter chicken": {
        "title": "Butter Chicken (Murgh Makhani)",
        "prep_time": "20 mins",
        "cook_time": "35 mins",
        "servings": "4",
        "ingredients": [
            "500g boneless chicken (cubed)",
            "1 cup yogurt",
            "1 tbsp lemon juice",
            "1 tsp red chili powder",
            "1 tsp garam masala",
            "1 tsp turmeric",
            "2 tbsp butter + 1 tbsp oil",
            "1 large onion (finely chopped)",
            "1 tbsp ginger-garlic paste",
            "400g canned tomato puree",
            "1 cup heavy cream",
            "1 tsp sugar",
            "1 tsp dried fenugreek leaves (kasuri methi)",
            "Salt to taste",
            "Fresh coriander for garnish"
        ],
        "steps": [
            "Marinate chicken with yogurt, lemon juice, turmeric, chili powder, and salt for at least 30 minutes (overnight is best).",
            "Grill or pan-sear the marinated chicken on high heat until lightly charred. Set aside.",
            "In the same pan, melt butter with oil. Sauté chopped onions until soft and golden.",
            "Add ginger-garlic paste and cook for 2 minutes until fragrant.",
            "Pour in the tomato puree. Cook on medium heat for 10-12 minutes until oil separates from the sides.",
            "Add garam masala, sugar, and salt. Stir well.",
            "Reduce heat to low. Pour in the heavy cream and stir gently to combine into a smooth, silky sauce.",
            "Add the cooked chicken pieces. Simmer on low heat for 10 minutes.",
            "Crush kasuri methi between your palms and sprinkle over the curry. Stir gently.",
            "Garnish with fresh coriander and a swirl of cream. Serve hot with naan or rice."
        ],
        "nutrition": {"calories": "490 kcal", "protein": "30g", "carbs": "12g", "fat": "35g", "fiber": "2g"},
        "tips": [
            "Charring the chicken adds a smoky tandoori flavor.",
            "Kasuri methi at the end is the secret to authentic butter chicken taste.",
            "Let the sauce simmer low and slow for the richest flavor."
        ]
    },
    "pasta carbonara": {
        "title": "Spaghetti Carbonara",
        "prep_time": "10 mins",
        "cook_time": "20 mins",
        "servings": "2",
        "ingredients": [
            "200g spaghetti",
            "150g pancetta or guanciale (diced)",
            "3 large egg yolks + 1 whole egg",
            "1 cup Pecorino Romano (finely grated)",
            "Freshly cracked black pepper",
            "Salt for pasta water"
        ],
        "steps": [
            "Bring a large pot of heavily salted water to a rolling boil. Cook spaghetti until al dente (1 minute less than package instructions).",
            "While pasta cooks, whisk egg yolks, whole egg, and grated Pecorino in a bowl until creamy. Add generous black pepper.",
            "In a cold pan, add diced pancetta. Turn heat to medium and render the fat slowly until crispy (about 8 minutes). Remove from heat.",
            "Reserve 1 cup of starchy pasta water before draining the spaghetti.",
            "Add drained spaghetti to the pancetta pan (OFF HEAT). Toss to coat in the rendered fat.",
            "Pour the egg-cheese mixture over the pasta. Toss vigorously, adding pasta water a splash at a time to create a creamy, glossy sauce.",
            "The residual heat will cook the eggs gently — never put it back on direct heat or you'll get scrambled eggs.",
            "Serve immediately with extra Pecorino and black pepper on top."
        ],
        "nutrition": {"calories": "480 kcal", "protein": "22g", "carbs": "45g", "fat": "24g", "fiber": "2g"},
        "tips": [
            "The #1 rule: NEVER add cream. True carbonara is egg and cheese only.",
            "Always toss off heat to avoid scrambling the eggs.",
            "Starchy pasta water is the key to a silky sauce."
        ]
    },
    "paneer butter masala": {
        "title": "Paneer Butter Masala",
        "prep_time": "15 mins",
        "cook_time": "25 mins",
        "servings": "3",
        "ingredients": [
            "250g paneer (cubed)",
            "2 large tomatoes (pureed)",
            "1 large onion (pureed)",
            "2 tbsp butter",
            "1 tbsp oil",
            "1 tbsp ginger-garlic paste",
            "1 cup heavy cream",
            "1 tsp red chili powder",
            "1 tsp garam masala",
            "1 tsp kasuri methi",
            "1 tsp sugar",
            "Salt to taste",
            "Fresh coriander for garnish"
        ],
        "steps": [
            "Heat butter and oil in a pan. Add ginger-garlic paste and sauté for 1 minute.",
            "Add onion puree and cook on medium heat for 5 minutes until golden.",
            "Add tomato puree, red chili powder, and salt. Cook for 10 minutes until oil separates.",
            "Add sugar and garam masala. Stir well.",
            "Pour in the cream and stir to form a smooth, rich gravy.",
            "Add paneer cubes and simmer for 5 minutes on low heat.",
            "Crush kasuri methi and sprinkle on top. Mix gently.",
            "Garnish with coriander and a drizzle of cream. Serve with naan or paratha."
        ],
        "nutrition": {"calories": "450 kcal", "protein": "18g", "carbs": "15g", "fat": "35g", "fiber": "2g"},
        "tips": [
            "Soak paneer in warm water for 10 mins to make it soft and spongy.",
            "Don't overcook paneer or it becomes rubbery.",
            "Blend the onion and tomato smooth for a restaurant-style texture."
        ]
    },
    "dosa": {
        "title": "Crispy Masala Dosa",
        "prep_time": "8 hours (fermentation)",
        "cook_time": "20 mins",
        "servings": "6 dosas",
        "ingredients": [
            "2 cups rice (soaked 6 hrs)",
            "1 cup urad dal (soaked 4 hrs)",
            "1 tsp fenugreek seeds",
            "Salt to taste",
            "Oil or ghee for cooking",
            "For filling: 3 boiled potatoes, 1 onion, mustard seeds, turmeric, curry leaves, green chilies"
        ],
        "steps": [
            "Soak rice and fenugreek seeds together for 6 hours. Soak urad dal separately for 4 hours.",
            "Grind urad dal first to a smooth, fluffy white paste. Then grind rice to a slightly coarse paste.",
            "Mix both batters, add salt, and let it ferment overnight (8-12 hours) in a warm place.",
            "For potato filling: Heat oil, add mustard seeds, curry leaves, chopped onions, green chilies. Sauté until golden. Add turmeric and mashed potatoes. Mix well.",
            "Heat a flat cast-iron tawa on high. Sprinkle water and wipe clean.",
            "Pour a ladleful of batter in the center and spread in concentric circles to make a thin crepe.",
            "Drizzle oil/ghee around the edges. Cook on medium-high until the bottom turns golden and crispy.",
            "Place the potato filling in the center. Fold the dosa over the filling.",
            "Serve hot with coconut chutney and sambar."
        ],
        "nutrition": {"calories": "180 kcal", "protein": "5g", "carbs": "30g", "fat": "4g", "fiber": "2g"},
        "tips": [
            "Good fermentation = good dosa. Keep batter in a warm spot.",
            "The tawa must be very hot, then slightly reduced before spreading batter.",
            "Use a cast-iron pan for the crispiest results."
        ]
    }
}

RECIPE_PROMPT = """You are a world-class chef and cooking instructor. Generate a detailed, structured recipe for: {dish}

You MUST respond in EXACTLY this format with these exact section headers. Do not deviate:

## [Recipe Title]

**Prep Time:** [time]
**Cook Time:** [time]  
**Servings:** [number]

### 📋 Ingredients
- [ingredient 1 with exact quantity]
- [ingredient 2 with exact quantity]
(list ALL ingredients needed)

### 👨‍🍳 Step-by-Step Instructions
1. [Detailed first step with temperatures, times, and visual cues]
2. [Detailed second step]
(number ALL steps clearly)

### 🔥 Nutrition Facts (per serving)
- Calories: [amount]
- Protein: [amount]
- Carbs: [amount]
- Fat: [amount]
- Fiber: [amount]

### 💡 Pro Tips
- [Helpful tip 1]
- [Helpful tip 2]
- [Helpful tip 3]

Be detailed, accurate, and include cooking temperatures, timing cues, and visual indicators in each step.
"""

def find_fallback_recipe(text):
    """Fuzzy match against pre-built recipes."""
    text = text.lower().strip()
    # Exact match first
    if text in PREBUILT_RECIPES:
        return PREBUILT_RECIPES[text]
    # Substring match
    for key, recipe in PREBUILT_RECIPES.items():
        if key in text or text in key:
            return recipe
    # Word overlap match
    text_words = set(text.split())
    best_match = None
    best_score = 0
    for key, recipe in PREBUILT_RECIPES.items():
        key_words = set(key.split())
        overlap = len(text_words & key_words)
        if overlap > best_score:
            best_score = overlap
            best_match = recipe
    if best_score > 0:
        return best_match
    return None

def format_fallback_as_text(recipe_dict):
    """Convert a fallback recipe dict to formatted text."""
    lines = []
    lines.append(f"## {recipe_dict['title']}\n")
    lines.append(f"**Prep Time:** {recipe_dict['prep_time']}")
    lines.append(f"**Cook Time:** {recipe_dict['cook_time']}")
    lines.append(f"**Servings:** {recipe_dict['servings']}\n")
    lines.append("### 📋 Ingredients")
    for ing in recipe_dict["ingredients"]:
        lines.append(f"- {ing}")
    lines.append("\n### 👨‍🍳 Step-by-Step Instructions")
    for i, step in enumerate(recipe_dict["steps"], 1):
        lines.append(f"{i}. {step}")
    lines.append("\n### 🔥 Nutrition Facts (per serving)")
    n = recipe_dict["nutrition"]
    lines.append(f"- Calories: {n['calories']}")
    lines.append(f"- Protein: {n['protein']}")
    lines.append(f"- Carbs: {n['carbs']}")
    lines.append(f"- Fat: {n['fat']}")
    lines.append(f"- Fiber: {n['fiber']}")
    if "tips" in recipe_dict:
        lines.append("\n### 💡 Pro Tips")
        for tip in recipe_dict["tips"]:
            lines.append(f"- {tip}")
    return "\n".join(lines)

def generate_recipe(user_text, lang):
    # Translate input to English for processing
    try:
        text_en = GoogleTranslator(source=lang, target="en").translate(user_text).lower()
    except Exception:
        text_en = user_text.lower()

    recipe_text = None

    try:
        # 1. AI Generation with new SDK
        prompt = RECIPE_PROMPT.format(dish=text_en)
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        if response and response.text:
            recipe_text = response.text
    except Exception as e:
        print(f"AI Generation Error: {e}")

    # 2. Fallback to pre-built recipes
    if not recipe_text:
        fallback = find_fallback_recipe(text_en)
        if fallback:
            recipe_text = format_fallback_as_text(fallback)
        else:
            recipe_text = f"""## {text_en.title()}

**Prep Time:** 15-20 mins
**Cook Time:** 30-40 mins
**Servings:** 2-4

### 📋 Ingredients
- Standard ingredients for {text_en}
- Seasonings and spices to taste
- Oil or butter for cooking

### 👨‍🍳 Step-by-Step Instructions
1. Prepare and wash all ingredients. Chop vegetables and measure out spices.
2. Heat oil or butter in a pan over medium heat.
3. Follow traditional cooking methods for {text_en}.
4. Season to taste with salt, pepper, and preferred spices.
5. Cook until done, checking for proper temperature and texture.
6. Let rest for a few minutes before serving.

### 🔥 Nutrition Facts (per serving)
- Calories: ~300-500 kcal
- Protein: ~15-25g
- Carbs: ~30-50g
- Fat: ~10-20g

### 💡 Pro Tips
- Always taste as you cook and adjust seasonings.
- Use fresh ingredients for the best flavor.
- Don't overcrowd the pan — cook in batches if needed.

*Note: This is a generic template. For a detailed recipe, please check your internet connection and try again.*
"""

    # 3. Translate back to user language
    if lang != "en":
        try:
            recipe_text = GoogleTranslator(source="en", target=lang).translate(recipe_text)
        except Exception:
            pass  # Return English if translation fails

    return recipe_text