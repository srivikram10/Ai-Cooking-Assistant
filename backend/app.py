import os
from flask import Flask, request, jsonify, render_template
from ai_engine import generate_recipe
from voice import voice_input, voice_output
from db import save_recipe
from validator import is_cooking_query

# This finds the absolute path of the 'backend' folder
base_dir = os.path.dirname(os.path.abspath(__file__))
# This points to the 'frontend' folder one level up
frontend_dir = os.path.abspath(os.path.join(base_dir, "..", "frontend"))

app = Flask(__name__, 
            template_folder=frontend_dir, 
            static_folder=frontend_dir,
            static_url_path='')

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get-recipe", methods=["POST"])
def get_recipe():
    data = request.json
    user_text = data.get("text", "")
    lang = data.get("lang", "en")

    if not user_text.strip():
        return jsonify({
            "recipe": "Please enter a dish name to get a recipe."
        }), 400

    # Restrict to cooking-related questions
    if not is_cooking_query(user_text):
        return jsonify({
            "recipe": "❌ I can only answer cooking-related questions."
        }), 400

    recipe = generate_recipe(user_text, lang)

    # Only try to save if the recipe isn't an error message
    if "AI Error" not in recipe and "generic template" not in recipe.lower():
        save_recipe(user_text, recipe)

    return jsonify({"recipe": recipe})

@app.route("/voice-recipe", methods=["POST"])
def voice_recipe():
    lang = request.json["lang"]
    user_text = voice_input(lang)
    recipe = generate_recipe(user_text, lang)
    save_recipe(user_text, recipe)
    voice_output(recipe, lang)
    return jsonify({"spoken_text": user_text, "recipe": recipe})

if __name__ == "__main__":
    app.run(debug=True)