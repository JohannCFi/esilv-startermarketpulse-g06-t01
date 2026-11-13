from pathlib import Path
import csv
import json


def load_instruments(filepath="/workspaces/esilv-startermarketpulse-g06-t01/data/sample/instruments.json"):
    """Load and parse JSON metadata file into a Python dictionary."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return json.load(file)
    

def load_prices(filepath="/workspaces/esilv-startermarketpulse-g06-t01/data/sample/prices.csv"):
    """Load market observations from CSV into a list of dictionaries."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))
    

def filter_prices(prices, ticker):
    """Filter observation dictionaries matching a specific ticker."""
    return [row for row in prices if row["ticker"] == ticker]


def get_first_close(prices):
    """
    Return the initial close price of a price series as a float.
    """
    if not prices:
        return 0.0
    return float(prices[0]["close"])


def get_last_close(prices):
    """
    Return the final close price of a price series as a float.
    """
    if not prices:
        return 0.0
    return float(prices[-1]["close"])