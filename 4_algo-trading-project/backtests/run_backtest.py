import backtrader as bt
from utils.fetch_data import fetch_data
from strategies.rsiEmaStrategy import rsiEmaStrategy
from strategies.rsiEmaIntradayStrategy import rsiEmaIntradayStrategy
from strategies.ROCMomentumStrategy import ROCMomentumStrategy

import pandas as pd

def run_backtest(strategy="", symbol="AAPL", start="2022-01-01", end="2023-01-01", interval="1d"):

    df = fetch_data(symbol, start, end, interval)
    df.columns = df.columns.droplevel(1)
    df['ema_20'] = df['Close'].ewm(span=20).mean()
    
    data_bt = bt.feeds.PandasData(dataname=df)

    cerebro = bt.Cerebro()
    cerebro.adddata(data_bt)
    cerebro.addstrategy(strategy)

    cerebro.broker.set_cash(100000)
    cerebro.addsizer(bt.sizers.PercentSizer, percents=10)

    portfolio_initial = cerebro.broker.getvalue()
    print(f"Starting Portfolio Value: ${portfolio_initial:,.2f}")
    results = cerebro.run()
    portfolio_final = cerebro.broker.getvalue()
    print(f"Final Portfolio Value: ${portfolio_final:,.2f}")
    
    profit_percent = (portfolio_final-portfolio_initial)/portfolio_initial*100
    print(f"Profit% : {profit_percent:.2f}%")

    return cerebro, results, profit_percent