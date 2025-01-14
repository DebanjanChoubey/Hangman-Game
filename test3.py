import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, quantity, buy_price):
        if ticker in self.portfolio:
            print(f"Stock {ticker} is already in your portfolio.")
        else:
            self.portfolio[ticker] = {'quantity': quantity, 'buy_price': buy_price}
            print(f"Added {ticker} with quantity {quantity} at buy price {buy_price}.")

    def remove_stock(self, ticker):
        if ticker in self.portfolio:
            del self.portfolio[ticker]
            print(f"Removed {ticker} from your portfolio.")
        else:
            print(f"Stock {ticker} is not in your portfolio.")

    def view_portfolio(self):
        print("\nPortfolio:")
        for ticker, details in self.portfolio.items():
            print(f"{ticker} - Quantity: {details['quantity']}, Buy Price: {details['buy_price']}")
        print()

    def track_performance(self):
        print("\nTracking Performance:")
        for ticker, details in self.portfolio.items():
            stock = yf.Ticker(ticker)
            current_price = stock.history(period="1d")['Close'].iloc[-1]
            profit_loss = (current_price - details['buy_price']) * details['quantity']
            print(f"{ticker}: Current Price: {current_price:.2f}, Profit/Loss: {profit_loss:.2f}")
        print()

def main():
    portfolio = StockPortfolio()
    while True:
        print("\nMenu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Track Performance")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            ticker = input("Enter stock ticker: ").upper()
            quantity = int(input("Enter quantity: "))
            buy_price = float(input("Enter buy price: "))
            portfolio.add_stock(ticker, quantity, buy_price)
        elif choice == "2":
            ticker = input("Enter stock ticker to remove: ").upper()
            portfolio.remove_stock(ticker)
        elif choice == "3":
            portfolio.view_portfolio()
        elif choice == "4":
            portfolio.track_performance()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
