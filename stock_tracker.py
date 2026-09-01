# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 180,
    "MSFT": 420
}

total_investment = 0

print("📈 Stock Portfolio Tracker")
print("--------------------------")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print("Stock price:", stock_prices[stock])
    print("Investment:", investment)

print("\n--------------------------")
print("💰 Total Investment:", total_investment)
print("--------------------------")
