"""
CodeAlpha Python Programming Internship
Task 2: Stock Portfolio Tracker

Lets the user "buy" stocks by entering a stock symbol and quantity.
Prices are hardcoded. Calculates total investment and saves a
summary report to a .txt file.
"""

from datetime import datetime

# Hardcoded stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420,
    "NFLX": 680,
    "META": 500,
}


def show_available_stocks():
    print("\nAvailable Stocks:")
    print(f"{'Symbol':<10}{'Price (USD)':>12}")
    print("-" * 22)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<10}{price:>12}")
    print()


def get_portfolio():
    portfolio = {}
    print("Enter stock symbol and quantity (type 'done' as symbol to finish).")

    while True:
        symbol = input("Stock symbol: ").strip().upper()
        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' not found in our price list. Try again.\n")
            continue

        qty_input = input(f"Quantity of {symbol}: ").strip()
        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("Please enter a valid positive whole number.\n")
            continue

        quantity = int(qty_input)
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.\n")

    return portfolio


def calculate_investment(portfolio):
    breakdown = {}
    total = 0
    for symbol, quantity in portfolio.items():
        cost = STOCK_PRICES[symbol] * quantity
        breakdown[symbol] = cost
        total += cost
    return breakdown, total


def display_summary(portfolio, breakdown, total):
    print("\nPortfolio Summary")
    print("=" * 40)
    print(f"{'Symbol':<10}{'Qty':>6}{'Price':>10}{'Value':>12}")
    print("-" * 40)
    for symbol, quantity in portfolio.items():
        print(f"{symbol:<10}{quantity:>6}{STOCK_PRICES[symbol]:>10}{breakdown[symbol]:>12}")
    print("-" * 40)
    print(f"{'Total Investment:':<26}{total:>14.2f}")


def save_report(portfolio, breakdown, total, filename="portfolio_report.txt"):
    with open(filename, "w") as f:
        f.write("Stock Portfolio Report\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 40 + "\n")
        f.write(f"{'Symbol':<10}{'Qty':>6}{'Price':>10}{'Value':>12}\n")
        f.write("-" * 40 + "\n")
        for symbol, quantity in portfolio.items():
            f.write(f"{symbol:<10}{quantity:>6}{STOCK_PRICES[symbol]:>10}{breakdown[symbol]:>12}\n")
        f.write("-" * 40 + "\n")
        f.write(f"{'Total Investment:':<26}{total:>14.2f}\n")
    print(f"\nReport saved to '{filename}'.")


def main():
    print("Welcome to the Stock Portfolio Tracker!")
    show_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks were added. Exiting.")
        return

    breakdown, total = calculate_investment(portfolio)
    display_summary(portfolio, breakdown, total)

    save_choice = input("\nSave this report to a .txt file? (y/n): ").strip().lower()
    if save_choice == "y":
        save_report(portfolio, breakdown, total)

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
