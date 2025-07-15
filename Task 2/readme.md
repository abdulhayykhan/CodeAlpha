# 📊 Task 2 – Stock Portfolio Tracker

This Python script simulates a basic **Stock Portfolio Tracker** that calculates total investment based on user input and a predefined dictionary of stock prices.

---

## ✅ Features

- Allows users to enter stock symbols and quantity of shares
- Uses hardcoded stock prices for calculation
- Validates input for symbol and quantity
- Calculates and displays total investment value
- Option to save portfolio summary to a `.txt` file

---

## 🧠 Concepts Used

- Python `dictionary` for storing stock prices
- `input()` and `print()` for user interaction
- `try-except` for error handling
- Loops and conditionals for control flow
- File handling (`open`, `write`) for optional saving to file

---

## 🧪 Logic Overview

- A dictionary like `{"AAPL": 180, "TSLA": 250}` defines stock prices
- User enters stock symbols (e.g., `AAPL`) and number of shares
- For each valid input:
  - The stock is added to a portfolio dictionary
  - Investment is calculated: `price × quantity`
- At the end, the program:
  - Displays a breakdown of investments
  - Shows the total portfolio value
  - Optionally writes this data to a `.txt` file

---

## 📸 Example Interaction

- 📈 Welcome to the Stock Portfolio Tracker
- Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN

- Enter stock symbol (or type 'done' to finish): AAPL
- Enter quantity of AAPL: 150

- Enter stock symbol (or type 'done' to finish): TSLA
- Enter quantity of TSLA: 56

- Enter stock symbol (or type 'done' to finish): GOOGL
- Enter quantity of TSLA: 456

- Enter stock symbol (or type 'done' to finish): done

- 💼 Your Portfolio:
- AAPL: 150 shares × $180 = $27000
- TSLA: 56 shares × $250 = $14000
- GOOGL: 456 shares × $250 = $59280

- 💰 Total Investment Value: $100280

- Do you want to save this summary to a text file? (yes/no): yes
- 📁 Portfolio summary saved to 'portfolio_summary.txt'

---

## 🙋‍♂️ Author

**Abdul Hayy Khan**  
Python Developer | CodeAlpha Intern

---

## 📜 License

This project was created as part of the **CodeAlpha Python Internship** and is intended for learning and demonstration purposes only
