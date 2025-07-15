# 🎮 Task 1 – Hangman Game

This is a simple text-based **Hangman Game** developed in Python as part of the CodeAlpha Python Internship Program.  
The user is challenged to guess a hidden word by entering one letter at a time, with a maximum of 6 incorrect guesses allowed.

---

## ✅ Features

- Randomly selects a word from a predefined list
- Displays progress using underscores for unguessed letters
- Allows up to 6 incorrect guesses
- Prevents repeated letter guesses
- Provides a **"Play Again"** option after each game session

---

## 🧠 Concepts Used

- `random` module for word selection
- `while` loop for game loop
- `if-else` conditions for guess validation
- `lists` for tracking guessed letters and word display
- String manipulation
- Functions to separate logic and improve readability

---

## 🧪 Logic Overview

- A word is randomly selected from a list of 5
- The user guesses one letter at a time
- If the letter exists in the word, all instances are revealed
- If the guess is incorrect, remaining tries decrease
- The game ends when:
  - The user guesses the full word correctly, or
  - The number of incorrect guesses reaches 6

---

## 📸 Example Interaction

- 🎮 Welcome to Hangman!
- Guess the word: _ _ _ _

- Enter a letter: a
- ❌ Wrong guess! Tries left: 5
- Word: _ _ _ _

- Enter a letter: o
- ✅ Correct guess!
- Word: _ o _ _

- Enter a letter: e
- ✅ Correct guess!
- Word: _ o _ e

- Enter a letter: x
- ❌ Wrong guess! Tries left: 4
- Word: _ o _ e

- Enter a letter: d
- ✅ Correct guess!
- Word: _ o d e

- Enter a letter: c
- ✅ Correct guess!
- Word: c o d e

- 🎉 Congratulations! You guessed the word: code

---

## 🙋‍♂️ Author

**Abdul Hayy Khan**  
Python Developer | CodeAlpha Intern

---

## 📜 License

This project was created as part of the **CodeAlpha Python Internship** and is intended for learning and demonstration purposes only.
