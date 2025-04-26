from utils.log_trade import log_trade
import backtrader as bt

class Rsi_ema_intraday(bt.Strategy):
    # Set strategy parameters (customize for intraday trading)
    params = (
        ("rsi_period", 14),        # RSI period, typically 14 for intraday
        ("ema_short_period", 7),   # Short-term EMA, 7-period
        ("ema_long_period", 21),   # Long-term EMA, 21-period for trend confirmation
        ("stop_loss", 0.01),       # Stop loss at 1% of price
        ("take_profit", 0.02),     # Take profit at 2% of price
    )

    def __init__(self):
        # Indicators
        self.rsi = bt.indicators.RSI(self.data.close, period=self.params.rsi_period)
        self.ema_short = bt.indicators.EMA(self.data.close, period=self.params.ema_short_period)
        self.ema_long = bt.indicators.EMA(self.data.close, period=self.params.ema_long_period)

        # Trade tracking
        self.order = None
        self.buy_price = None
        self.buy_date = None

        self.trades = []  # Store completed trades here!

    def next(self):
        # Skip bars until indicators are ready
        if len(self) < self.params.rsi_period + self.params.ema_long_period:
            return
        
        # Check if there is an open position
        if self.position.size == 0:
            # Buy signal: RSI < 30 (oversold) and price above short-term EMA and long-term EMA (bullish trend)
            if self.rsi[0] < 30 and self.data.close[0] > self.ema_short[0] and self.ema_short[0] > self.ema_long[0]:
                self.buy_price = self.data.close[0]
                self.buy_date = self.data.datetime.date(0)
                self.order = self.buy()
                
                # Apply stop-loss and take-profit orders
                stop_loss_price = self.buy_price * (1 - self.params.stop_loss)
                take_profit_price = self.buy_price * (1 + self.params.take_profit)
                self.sell(
                    exectype=bt.Order.Stop, price=stop_loss_price, parent=self.order
                )
                self.sell(
                    exectype=bt.Order.Limit, price=take_profit_price, parent=self.order
                )
        
        # Sell signal: RSI > 70 (overbought) and price below short-term EMA and long-term EMA (bearish trend)
        elif self.position.size > 0:
            if self.rsi[0] > 70 and self.data.close[0] < self.ema_short[0] and self.ema_short[0] < self.ema_long[0]:
                sell_price = self.data.close[0]
                sell_date = self.data.datetime.date(0)
                self.order = self.sell()
                
                # Record trade info
                profit = sell_price - self.buy_price
                log_trade(self.trades, self.buy_date, self.buy_price, sell_date, sell_price, profit)

    def stop(self):
        # At the end, if any position is still open, report it
        if self.position.size > 0:
            current_price = self.data.close[0]
            current_date = self.data.datetime.date(0)
            unrealized_profit = (current_price - self.buy_price)
            log_trade(self.trades, self.buy_date, self.buy_price, current_date, current_price, unrealized_profit)