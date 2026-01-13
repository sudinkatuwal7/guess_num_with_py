# 🎯 Number Guessing Game (Python)

A simple **console-based number guessing** game built using Python.  
The computer randomly selects a number between **1 and 100**, and the player must guess it within a limited number of attempts based on the chosen difficulty.

---

## 📌 Features

- Random number generation between 1 and 100
- Two difficulty levels:
  - **Easy** → 10 attempts
  - **Hard** → 5 attempts
- Feedback after each guess (Too High / Too Low)
- Clear win and lose conditions
- ASCII logo support using a separate `art.py` file

---

## 🕹️ How to Play

1. Run the program.
2. Choose a difficulty:
   - Type `easy` for 10 attempts
   - Type `hard` for 5 attempts
3. Enter a number between **1 and 100**.
4. The game will guide you by telling whether your guess is too high or too low.
5. The game ends when:
   - You guess the correct number ✅
   - You run out of attempts ❌

---

## 📂 Project Structure

```text
number-guessing-game/
├── main.py      # Main game logic
├── art.py       # Contains ASCII logo
└── README.md    # Project documentation
```

## ▶️ How to Run the Game

Make sure **Python 3** is installed on your system.
```bash
python main.py
