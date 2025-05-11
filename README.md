# Quizz-game
Tkinter Quiz Game
This is a simple True/False quiz game built using Python's tkinter library. It fetches questions from the Open Trivia Database API and displays them in a graphical user interface (GUI).

🧩 Features
Clean GUI built with tkinter

True/False questions loaded from an online API

Score tracking

Feedback with color changes

End-of-quiz message

🌐 Where the Questions Come From
The app fetches 10 True/False questions from the Open Trivia Database using this URL:

bash
Copy
Edit
https://opentdb.com/api.php?amount=10&type=boolean
📄 Files Overview
main.py: Entry point, sets up the quiz logic and GUI.

question_model.py: Represents a question object.

quiz_brain.py: Handles quiz logic like score and answer checking.

data.py: Fetches and prepares quiz data from the API.

ui.py: Builds and manages the GUI using tkinter.
