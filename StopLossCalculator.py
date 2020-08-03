import yfinance as yf
import math


class StopLossCalculator:
    def __init__(self):
        pass

    def run(self):
        ticker = input("Ticker: ").upper()
        try:
            data = yf.Ticker(ticker)
            info = data.info
            money_to_invest = input("Money to Invest (USD): ")
            try:
                money_to_invest = float(money_to_invest)
                max_loss = input("Max Loss (USD): ")
                try:
                    max_loss = float(max_loss)
                    regular_market_price = info["regularMarketPrice"]

                    shares_to_buy = math.floor(money_to_invest / regular_market_price)
                    if shares_to_buy <= 0:
                        print("Insufficient funds to purchase 1 share")
                        return

                    max_price_movement_per_share = math.floor(max_loss / shares_to_buy)

                    buy_price = regular_market_price
                    stop_price = buy_price - max_price_movement_per_share

                    print("RESULTS:")
                    print("- Buy " + str(shares_to_buy) + " shares of " + ticker + " for $" + str(buy_price))
                    print("- Set your stop loss at $" + str(stop_price))
                except ValueError:
                    print("Error: Max loss must be a number or decimal.")
            except ValueError:
                print("Error: Money to Invest must be a number or decimal.")

        except ValueError:
            print("Error: Ticker " + ticker + " not found")
        except IndexError:
            print("Error: Ticker data could not be loaded for " + ticker)
