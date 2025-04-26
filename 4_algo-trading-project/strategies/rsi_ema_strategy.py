
import backtrader as bt

class RSIEMAStrategy(bt.Strategy):
    params = dict(rsi_period=14, ema_period=20, rsi_overbought=70, rsi_oversold=30)

    def __init__(self):
        self.rsi = bt.ind.RSI(period=self.params.rsi_period)
        self.ema = bt.ind.EMA(period=self.params.ema_period)

    def next(self):
        if not self.position:
            if self.rsi < self.params.rsi_oversold and self.data.close > self.ema:
                self.buy()
        elif self.rsi > self.params.rsi_overbought and self.data.close < self.ema:
            self.sell()
