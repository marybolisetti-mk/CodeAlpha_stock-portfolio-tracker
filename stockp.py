stock_prices = {
    "RELIANCE": 2500,
    "TCS": 3800,
    "HDFC": 1650,
    "INFY": 1450,
    "ICICIBANK": 1100,
    "WIPRO": 520,
    "SUNPHARMA": 1750,
    "TATAMOTORS": 980
}
total_investment = 0
print("Stock Portfolio Tracker")
print("Available stocks:", list(stock_prices.keys()))
while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not available! Please choose from the list.")
        continue
    quantity = int(input("Enter quantity: "))
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"Added {stock} - {quantity} shares @ ₹{price} = ₹{investment}")
print("\n" + "="*40)
print(f"Total Investment Value: ₹{total_investment}")
print("="*40)
with open("portfolio.txt", "w") as file:
    file.write(f"Stock Portfolio Summary\n")
    file.write(f"{'='*40}\n")
    file.write(f"Total Investment Value: ₹{total_investment}\n")
    file.write(f"\nStocks owned:\n")
print("Data saved to portfolio.txt")