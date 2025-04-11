# 🎓 Console Quiz Application
                "Console-based quiz app with categories, leaderboard, timer &amp; color themes 🌈✨"
An interactive command-line quiz game built with Python! Test your knowledge in different categories like Python and General Knowledge.

---

## :surfer: Features

- Multiple choice questions (MCQs)
- ⏱ Timed input with countdown `inputimeout`
- 🌈 Colorful console design using `colorama`
- ✅ Feedback on correct/incorrect answers
- 📂 File handling to persist scores and leaderboard 
- 🏆 Leaderboard storing top scores per category
 🧠 Multiple categories: Python & General Knowledge
- 🔧 Command-line support using `argparse` (CLI)
- Highlights player name on leaderboard if in top 3

---

## 🚀 How to Run [🛠️ Installation]

1. **Clone the repository:**

```bash
git clone https://github.com/garima57/quiz-app-pract.git
cd quiz-app-pract
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, manually install:
```bash
pip install inputimeout colorama
```

---

## 💡 Usage

### 🎮 Run interactively:
```bash
python quiz.py
```

### ⚙️ Run with command-line arguments:
```bash
python quiz.py --name "Alice" --category "Python"
```

> When using `--name` and `--category`, the quiz starts immediately without extra prompts.

---

## 📷 Screenshots

### Main Banner
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨       🎓 Welcome to the Quiz Application!       ✨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Sample Question
```
Q1: What does the 'len()' function do in Python?
A. Calculates length of string or list
B. Logs error
C. Creates list
D. Converts to int
```

### Leaderboard
```
🏆 Leaderboard:
1. Alice (Python) - 9/10
2. Bob (General Knowledge) - 8/10
3. Garima (Python) - 7/10
```
### 📊 Score Storage
```
All scores are saved to scores.txt after each quiz attempt.
To see how the format works without affecting actual data, refer to:

👉 scores_preview.txt
```
---

## 📁 File Structure

```bash
quiz-app-pract/
├── quiz.py                    # Main Python file
├── scores.txt                 # Persistent leaderboard data
├── python_questions.txt       # Category: Python
├── general_knowledge_questions.txt  # Category: GK
├── .gitignore
├── README.md
└── requirements.txt           # List of dependencies (optional)
```

---

## 🌱 Development

If you want to experiment or add new features:

1. Create a new branch:
```bash
git checkout -b feature/new-mode
```

2. Make your changes, commit, and push:
```bash
git add .
git commit -m "Add new game mode"
git push origin feature/new-mode
```

3. Create a pull request on GitHub to merge your changes.

---

## 🙌 Contributions

Ideas, suggestions, and contributions are welcome! You can fork this repo, improve features, or open issues if you find bugs.

---

## 👩‍💻 Made with ❤️ by [garima](https://github.com/garima57)

