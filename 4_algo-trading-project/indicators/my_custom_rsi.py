
import backtrader as bt

# Use custom indicators only for advanced uses
# Strictly not required for beginners
class CustomRSI(bt.Indicator):
    lines = ('rsi',)
    params = dict(period=14)

    def __init__(self):
        self.lines.rsi = bt.indicators.RSI_SMA(self.data.close, period=self.p.period)
