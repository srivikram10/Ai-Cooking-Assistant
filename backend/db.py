import mysql.connector
from config import DB_CONFIG

def save_recipe(user_text, recipe):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO recipes (query, recipe) VALUES (%s, %s)",
            (user_text, recipe)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        # This prevents the app from stopping if the database fails
        print(f"Database Error (Recipe not saved): {e}")