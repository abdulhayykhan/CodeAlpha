# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 310,
    "AMZN": 140
}

# Store user portfolio
portfolio = {}

print("📈 Welcome to the Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("❌ Stock not found. Please enter a valid stock symbol.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("❌ Please enter a valid positive integer for quantity.")
        continue

    # Add or update stock in portfolio
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

# Calculate total investment
total_investment = 0
print("\n💼 Your Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optional: Save to text file
save = input("\nDo you want to save this summary to a text file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as file:
        file.write("Your Stock Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")
    print("📁 Portfolio summary saved to 'portfolio_summary.txt'")
    