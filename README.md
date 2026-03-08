# 🧠 Trivia Game (Python)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Project-Completed-success)

A **console-based trivia game** written in Python, featuring multiple players, score tracking, and two categories:

- **General Knowledge**
- **Computer Science**

Players take turns answering questions. Points are awarded for correct answers, and the player with the highest score wins.

---

# 🛠 Features

### Categories
- **General Knowledge**  
- **Computer Science**  

### Multiplayer
- Supports 2 or more players  
- Players answer in **round-robin order**

### Question Rotation
- Alternates between categories every 7 questions

### Input Validation
- Only accepts valid answers: `A`, `B`, `C`, or `D`

### Scoreboard
- Displays scores after each round  
- Declares the winner at the end of the game

---

# 🎮 How It Works

1. Players enter their **names**  
2. Choose the **initial category**  
3. Players take turns answering questions  
4. Correct answers award points; wrong answers switch the turn  
5. After 14 rounds (7 questions per category), the **winner** is displayed  

---

# 📂 Project Structure

```
trivia-game
│
├── trivia_game.py
└── README.md
```

---

# 🖥 Example Gameplay

```
**********************************
Game starts

How many players will be playing this game ? (min 2)
2

What is player #1's name ?
Alice
What is player #2's name ?
Bob

Alice can choose the topic
1: General knowledge 
2: Computer Science: 1

**********************************
Round #1
Question: What is the capital of France?

A: Berlin
B: London
C: Paris
D: Madrid

Alice's answer: C
CORRECT !!!

Current Scores:
Alice: 1
Bob: 0
**********************************
```

After 14 rounds, the winner is announced.

---

# 🧠 Implementation Details

- **Classes Used**:
  - `Game` – Handles gameplay, category rotation, and scoring  
  - `Player` – Tracks each player’s name, points, and current turn  
  - `Question` – Manages question display and solutions  

- **Validation**:
  - Players can only select answers `A`, `B`, `C`, or `D`  
  - Ensures at least **2 players**  

- **Category Switching**:
  - After 7 questions, the topic switches automatically between General Knowledge and Computer Science

---

# ▶️ Running the Game

1. Ensure **Python 3.x** is installed
2. Install dependencies:

```
pip install colorama
```

3. Run the game:

```
python trivia_game.py
```

4. Follow the prompts in the console

---

# 🎯 Learning Goals

- Practice **object-oriented programming** in Python  
- Handle **user input validation**  
- Manage **game state and scoring**  
- Implement **dynamic question rotation and multiplayer logic**

---

# 🔮 Possible Improvements

- Add more categories and questions  
- Implement **timer-based answering**  
- Add **GUI interface** using `tkinter` or `NiceGUI`  
- Save scores and allow **multiple game sessions**  
- Randomize questions instead of fixed order  

---

# 👨‍💻 Author

Student project focused on learning **Python fundamentals**, **game logic**, and **multiplayer interaction** in a console environment.
