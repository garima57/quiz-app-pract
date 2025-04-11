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


![image](https://github.com/user-attachments/assets/c6622f50-2a97-4d92-a7fe-c420faf066d8)

![image](https://github.com/user-attachments/assets/5ee8f55b-3c6e-413a-b9ab-880b3159f09f)

![Screenshot 2025-04-11 233805](https://github.com/user-attachments/assets/73374ce0-f811-44fe-910c-6cbe398c339c)

![Screenshot 2025-04-11 233820](https://github.com/user-attachments/assets/970dab79-bc46-46e1-b475-22f27f4bef5c)

![Screenshot 2025-04-11 233842](https://github.com/user-attachments/assets/fff6de59-d62b-4e46-b14f-ec996b7cfdec)

![image](https://github.com/user-attachments/assets/c2147389-fd1b-47c6-806b-12856d779f9c)


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

To use it, rename to `scores.txt` locally. It is `.gitignored` to avoid uploading real user data
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

## ✅ Project Highlights

### 1. **Functionality**
- 🎯 Supports multiple categories (Python, General Knowledge)
- ⏰ Timed questions with input timeout handling
- ✅ Score tracking with a persistent leaderboard
- 🏆 Category-wise performance and top 3 highlighting

### 2. **Creativity & Additional Features**
- 🎨 Visually styled console using emojis and `colorama`
- 📂 Category system and question loading from external files

### 3. **Code Quality & File Handling**
- 🧼 Clean, modular code with comments and readable variable names
- 📁 Uses `scores.txt` for persistent storage (excluded via `.gitignore`)
- ❌Proper error handling for missing files and bad inputs
- 🧩 Uses `argparse`, `os`, file I/O, and other Python features

### 4. **Testing & Stability**
- ✅ Tested with different categories, inputs, and edge cases
- ❌ Invalid inputs and timeouts handled 
- 🔁 Includes a replay option to encourage re-engagement


---

## 📜 License
```
This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
```
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
Happy Quizzing! 🎉
## 👩‍💻 Made with ❤️ by [garima](https://github.com/garima57)

