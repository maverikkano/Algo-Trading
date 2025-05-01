# 01-May-2025 00:00

from backtests.run_backtest import run_backtest
from strategies.rsiEmaStrategy import rsiEmaStrategy
from utils.savePlot import save_backtest_plot
from utils.extractTrades import extractTrades
import os

plot_info = {
    "strategy": rsiEmaStrategy,
    "symbol": "TSLA",
    "start_date": "2020-01-01",
    "end_date": "2025-01-01",
    "profit%": 0,
    "trades": {},
}

cerebro, results, profit_percent = run_backtest(strategy=plot_info["strategy"], symbol=plot_info["symbol"], start=plot_info["start_date"], end=plot_info["end_date"])

plot_info["profit%"] = profit_percent
plot_info["trades"] = extractTrades(results=results)

save_backtest_plot(cerebro, os.path.abspath(__file__), plot_info)