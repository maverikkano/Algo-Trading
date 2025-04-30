import backtrader as bt

class ROCMomentumStrategy(bt.Strategy):
    params = dict(
        roc_period=20,
        ema_period=50,
        roc_threshold=5  # Minimum % change to trigger momentum entry
    )

    def __init__(self):
        self.roc = bt.ind.RateOfChange100(period=self.params.roc_period)
        self.ema = bt.ind.EMA(period=self.params.ema_period)

    def next(self):
        if not self.position:
            if self.roc > self.params.roc_threshold and self.data.close > self.ema:
                self.buy()
        elif self.roc < 0 and self.data.close < self.ema:
            self.sell()