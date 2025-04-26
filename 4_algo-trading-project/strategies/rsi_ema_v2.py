from utils.log_trade import log_trade
import backtrader as bt

class Rsi_ema_v2(bt.Strategy):
    params = (
        ("rsi_period", 14),
        ("ema_period", 7),
    )

    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data.close, period=self.params.rsi_period)
        self.ema = bt.indicators.EMA(self.data.close, period=self.params.ema_period)

        # Trade tracking
        self.order = None
        self.buy_price = None
        self.buy_date = None

        self.trades = []  # Store completed trades here!


    def next(self):
        # Skip bars until indicators are ready
        if len(self) < self.params.rsi_period + 7:   # say 14 for RSI + a few more for safety
            return
        
        if self.position.size == 0:
            if self.rsi[0] > 70 or self.data.close[0] < self.ema[0]:
                self.buy_price = self.data.close[0]
                self.buy_date = self.data.datetime.date(0)
                self.order = self.buy()
        else:
            if self.rsi[0] < 30 and self.data.close[0] > self.ema[0]:
                sell_price = self.data.close[0]
                sell_date = self.data.datetime.date(0)
                self.order = self.sell()

                # Record trade info
                profit = sell_price - self.buy_price
                log_trade(self.trades, self.buy_date, self.buy_price, sell_date, sell_price, profit)

    def stop(self):
        # At the end, if any position is still open, just report it
        if self.position.size > 0:
            current_price = self.data.close[0]
            current_date = self.data.datetime.date(0)

            unrealized_profit = (current_price - self.buy_price)

            log_trade(self.trades, self.buy_date, self.buy_price, current_date, current_price, unrealized_profit)