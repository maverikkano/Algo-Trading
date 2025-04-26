
import yfinance as yf
import pandas as pd

def fetch_data(symbol, start, end, timeframe="1d"):
    df = yf.download(symbol, start=start, end=end, interval=timeframe)
    df.dropna(inplace=True)
    return df
