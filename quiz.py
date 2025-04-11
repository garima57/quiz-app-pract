# -*- coding: utf-8 -*-
import os
import time
import argparse
from colorama import init, Fore, Style
init(autoreset=True)

GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
RESET = Style.RESET_ALL

# Try inputimeout for better input handling
try:
    from inputimeout import inputimeout, TimeoutOccurred

    def timed_input(prompt, timeout=10):
        print(f"You have {timeout} seconds to answer.")
        try:
            return inputimeout(prompt=prompt, timeout=timeout)
        except TimeoutOccurred:
            print("\n⏰ Time's up!")
            return None
except ImportError:
    print("Install `inputimeout` for better timeout handling. Falling back to regular input.")

    def timed_input(prompt, timeout=10):
        return input(prompt)

# 🧠 Function to load questions

def load_questions(category):
    filename = f"{category.lower().replace(' ', '_')}_questions.txt"
    questions = []
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return questions

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 6:
                q, a, b, c, d, correct = parts
                questions.append({
                    "question": q,
                    "options": [a, b, c, d],
                    "correct": correct.upper()
                })
    return questions


def give_feedback(score, total):
    percent = (score / total) * 100
    if percent == 100:
        print(f"{CYAN}🏆 Perfect Score! You’re a quiz master!{RESET}")
    elif percent >= 80:
        print(f"{CYAN}🎯 Great job! You really know your stuff!{RESET}")
    elif percent >= 50:
        print(f"{CYAN}👍 Not bad! A little more practice and you’re there!{RESET}")
    else:
        print(f"{CYAN}📚 Keep learning! You’ll get it next time!{RESET}")

# 🎨 Styled banner

def print_banner(text):
    border = "━" * 50
    print(f"\n{CYAN}{border}")
    print(f"✨ {text.center(46)} ✨")
    print(f"{border}{RESET}\n")

# 🏆 Leaderboard display

def show_leaderboard(current_user):
    print("\n🏆 Leaderboard:")
    try:
        with open("scores.txt", "r") as file:
            scores = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name, category, score_str = parts
                    try:
                        correct, total = map(int, score_str.split('/'))
                        scores.append((name, category, correct, total))
                    except:
                        continue

            scores.sort(key=lambda x: x[2], reverse=True)

            if not scores:
                print("No scores yet.")
                return

            for i, (name, category, correct, total) in enumerate(scores[:3], start=1):
                highlight = GREEN + Style.BRIGHT if name == current_user else ""
                reset = RESET if name == current_user else ""
                print(f"{highlight}{i}. {name} ({category}) - {correct}/{total}{reset}")

    except FileNotFoundError:
        print("Leaderboard not available (scores.txt missing).")

# 🧠 Main quiz logic

def main():
    parser = argparse.ArgumentParser(description="Console-based Quiz Application")
    parser.add_argument('--name', type=str, help='Your name')
    parser.add_argument('--category', type=str, choices=["Python", "General Knowledge"], help='Quiz category')
    args = parser.parse_args()

    use_args = False
    if args.name and args.category:
        use_args = True
        print(f"{CYAN}ℹ️  Using command-line arguments: Name = {args.name}, Category = {args.category}{RESET}")

    print_banner("🎓 Welcome to the Quiz Application!")
    print("Rules:\n- Each question has 4 options.\n- Enter the option (A, B, C, D) as your answer. Type 'quit' to exit anytime.")
    if not use_args:
        input("Press Enter to Start!\n")

    name = args.name if use_args else input("Enter your name: ").strip()
    categories = ["Python", "General Knowledge"]
    category = args.category if use_args else None

    if not category:
        print("\nAvailable Categories:")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        cat_choice = input("Choose a category (1 or 2): ").strip()
        if cat_choice not in ['1', '2']:
            print("Invalid category. Exiting.")
            return
        category = categories[int(cat_choice)-1]

    print(f"\n📂 Category Selected: {category}\n")

    questions = load_questions(category)
    if not questions:
        print("No questions loaded. Exiting.")
        return

    score = 0

    for i, q in enumerate(questions, start=1):
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\nQ{i}: {q['question']}")
        print(f"A. {q['options'][0]}")
        print(f"B. {q['options'][1]}")
        print(f"C. {q['options'][2]}")
        print(f"D. {q['options'][3]}")

        answer = timed_input("Your Answer (A/B/C/D): ", timeout=15)
        if answer and answer.strip().lower() == "quit":
            print("\n👋 You chose to quit. Thanks for playing!")
            break

        if not answer:
            print(f"❌ You didn’t answer. The correct answer was: {q['correct']}\n")
            continue
        else:
            answer = answer.strip().upper()

        if answer == q['correct']:
            print(f"{GREEN}✅ Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}❌ Wrong! The correct answer was: {q['correct']}{RESET}\n")

    print_banner("🎉 Quiz Complete!")
    print(f"📂 Category: {category}")
    print(f"📊 Your Score: {score}/{len(questions)}")
    give_feedback(score, len(questions))

    try:
        with open("scores.txt", "a") as score_file:
            score_file.write(f"{name},{category},{score}/{len(questions)}\n")
        print("📝 Score recorded in scores.txt")
    except Exception as e:
        print("Error saving score:", e)

    show_leaderboard(current_user=name)

    play_again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("\n👋 Thanks for playing! See you again!")

# Run it
if __name__ == "__main__":
    main()
