from module import load_instruments, get_first_close, load_prices, filter_prices, get_last_close

def display_market_summary(asset, prices, show_currency=True):
    """
    Display a standardized market summary for any instrument or benchmark.
    
    Args:
        asset (dict): Metadata dictionary (containing 'ticker', 'name', 'currency').
        prices (list): Filtered observation dictionaries.
        show_currency (bool): Whether to append the currency code to prices.
    """
    first_close = get_first_close(prices)
    last_close = get_last_close(prices)
    currency_suffix = f" {asset.get('currency', '')}" if show_currency else ""

    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Observations : {len(prices)}")
    print(f"First close  : {first_close:.2f}{currency_suffix}")
    print(f"Last close   : {last_close:.2f}{currency_suffix}")

def run_td04_market_snapshot():
    """Simulate the complete main() workflow for TD02."""
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    print("=== MarketPulse ===")
    print()
    print("Market configuration")
    print("Period   : 1 month")
    print("Interval : Daily")
    print()
    print("Instrument")
    display_market_summary(instrument, instrument_prices, show_currency=True)
    print()
    print("Benchmark")
    display_market_summary(benchmark, benchmark_prices, show_currency=False)

run_td04_market_snapshot()