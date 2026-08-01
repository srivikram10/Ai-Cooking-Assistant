# 🍳 AI Cooking Assistant

An intelligent multilingual cooking assistant powered by **Google Gemini AI** that generates **detailed, step-by-step recipes** with ingredients, nutrition facts, and pro tips — all in a stunning dark-mode UI.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-2.0--flash-orange?logo=google&logoColor=white)

---

## ✨ Features

- 🤖 **AI-Powered Recipes** — Get detailed recipes for any dish using Google Gemini 2.0 Flash
- 📋 **Step-by-Step Instructions** — Numbered cooking steps with timing, temperatures & visual cues
- 🥗 **Nutrition Facts** — Calories, protein, carbs, fat & fiber per serving
- 💡 **Pro Tips** — Expert cooking tips for every recipe
- 🌐 **16 Languages** — English, Hindi, Tamil, Telugu, Malayalam, Kannada, Marathi, Bengali, Gujarati, French, Spanish, German, Japanese, Korean, Chinese & Arabic
- 🎤 **Voice Input** — Speak your dish name and get the recipe read back to you
- 🔍 **Quick Categories** — One-click buttons for popular dishes (Biryani, Pasta, Sushi, Pizza, etc.)
- 🎨 **Premium Dark UI** — Glassmorphism cards, gradient accents, smooth animations
- 📱 **Fully Responsive** — Works on desktop, tablet & mobile

---

## ⚙️ Tech Stack

| Layer        | Technology                                      |
|--------------|------------------------------------------------|
| **Frontend** | HTML5, CSS3 (dark mode, glassmorphism), Vanilla JS |
| **Backend**  | Flask (Python)                                  |
| **AI Model** | Google Gemini 2.0 Flash (`google-genai` SDK)    |
| **Translation** | Deep Translator (Google Translate API)       |
| **Voice**    | gTTS (Text-to-Speech) + SpeechRecognition       |
| **Database** | MySQL (optional, for saving recipe history)     |
| **Fonts**    | Google Fonts (Outfit + Inter)                   |

---

## 📁 Project Structure

```
Ai-Cooking-Assistant/
├── backend/
│   ├── app.py              # Flask server & API routes
│   ├── ai_engine.py        # Gemini AI integration & recipe generation
│   ├── config.py           # Environment config & DB settings
│   ├── db.py               # MySQL database helper
│   ├── voice.py            # Voice input/output (STT + TTS)
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── index.html           # Main HTML page
│   ├── style.css            # Premium dark-mode styles
│   ├── script.js            # Recipe rendering & UI logic
│   └── static/              # Static assets
├── database/
│   └── schema.sql           # MySQL table schema
├── .env.example             # Environment variable template
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Ai-Cooking-Assistant.git
cd Ai-Cooking-Assistant
```

### 2. Set up your API key

Get a free API key from [Google AI Studio](https://aistudio.google.com/), then create the `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and paste your key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Install dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 4. Run the server

```bash
python app.py
```

### 5. Open in browser

Go to **http://127.0.0.1:5000** and start cooking! 🎉

---

## 🗄️ Database Setup (Optional)

The app works without a database. If you want to save recipe history:

1. Install MySQL and create a database:
   ```sql
   CREATE DATABASE ai_cooking;
   ```

2. Run the schema:
   ```bash
   mysql -u root -p ai_cooking < database/schema.sql
   ```

3. Update the database password in `backend/config.py` if needed.

---

## 🌐 Supported Languages

| Language | Code | Language | Code |
|----------|------|----------|------|
| English | `en` | Marathi | `mr` |
| Hindi | `hi` | Bengali | `bn` |
| Tamil | `ta` | Gujarati | `gu` |
| Telugu | `te` | French | `fr` |
| Malayalam | `ml` | Spanish | `es` |
| Kannada | `kn` | German | `de` |
| Japanese | `ja` | Korean | `ko` |
| Chinese | `zh-CN` | Arabic | `ar` |

---

## 🔒 Security

- API keys are stored in `.env` (never committed to git)
- `.env.example` is provided as a template for developers
- All secrets are loaded via `python-dotenv`

---

