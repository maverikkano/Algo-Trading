# 01-May-2025 00:00

from backtests.run_backtest import run_backtest
from strategies.rsi_ema_v2 import Rsi_ema_v2
from utils.savePlot import save_backtest_plot
import os

cerebro = run_backtest(strategy=Rsi_ema_v2, symbol="AAPL", start="2020-01-01", end="2023-01-01")
save_backtest_plot(cerebro, os.path.abspath(__file__))