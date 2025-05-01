from utils.log_trade import log_trade
import backtrader as bt

class strategyName(bt.Strategy):

    # Essential parameters for the strategy
    params = (
        ("rsi_period", 14),
        ("ema_period", 7),
    )

    def __init__(self):

        # Initializing indicators (➡️ change this)
        self.rsi = bt.indicators.RSI(self.data.close, period=self.params.rsi_period)
        self.ema = bt.indicators.EMA(self.data.close, period=self.params.ema_period)

        # Trade tracking (✅ fixed)
        self.order = None
        self.buy_price = None
        self.buy_date = None
        self.trades = []  # Store completed trades here!


    def next(self):
        # warm up period if applicable for indicators (➡️ change this)
        warmup_period = max(self.params.rsi_period, self.params.ema_period)
        if len(self) < warmup_period:
            return
        
        if self.position.size == 0:
            if self.rsi[0] > 60:    #strategy- buying logic (➡️ change this)
                
                # collect info for logging (✅ fixed)
                self.buy_price = self.data.close[0] 
                self.buy_date = self.data.datetime.date(0)
                self.order = self.buy()
        
        else:
            if self.rsi[0] < 40 : #strategy- selling logic (➡️ change this)
                
                # collect info for logging (✅ fixed)
                sell_price = self.data.close[0]
                sell_date = self.data.datetime.date(0)
                self.order = self.sell()

                # Record trade info upon selling (✅ fixed)
                profit_percent = (sell_price - self.buy_price) / self.buy_price * 100
                log_trade(self.trades, self.buy_date, self.buy_price, sell_date, sell_price, profit_percent)

    # At the end, if any position is still open, just report it (✅ fixed)
    def stop(self):
        if self.position.size > 0:
            current_price = self.data.close[0]
            current_date = self.data.datetime.date(0)

            unrealized_profit = (current_price - self.buy_price)

            log_trade(self.trades, self.buy_date, self.buy_price, current_date, current_price, unrealized_profit)