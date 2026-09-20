# ⭕ Tic-Tac-Toe

A Python-based Tic-Tac-Toe game that started as a **Tkinter desktop application** and is being upgraded into a **Streamlit web application**.

The project includes Human vs Human and Human vs Computer gameplay, with a progressively improved computer opponent.



## ✨ Features

- 👥 Human vs Human mode
- 🤖 Human vs Computer mode
- 🧠 Computer opponent with strategic move selection
- 🏆 Win detection
- 🤝 Tie detection
- 🔄 Restart / Play Again
- 🎯 3×3 Tic-Tac-Toe board
- 🌐 Streamlit browser version
- 💻 Original Tkinter desktop version

## 🧠 Computer AI

The computer opponent uses a priority-based decision system.

### Current AI logic

1. Check if the computer can win
2. Check if the player can win and block them
3. Take the center
4. Take an available corner
5. Take an available edge

This allows the computer to make decisions based on the current board rather than simply choosing a random square.

## 🛠️ Technologies Used

- Python
- Tkinter
- Streamlit

## 📁 Project Structure

```text
Tic-Tac-Toe/
│
├── tic tac toe.py      # Original Tkinter version
├── st_app.py           # Streamlit web version
├── README.md

