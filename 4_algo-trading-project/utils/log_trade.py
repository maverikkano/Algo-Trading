def log_trade(trades, buy_date, buy_price, sell_date, sell_price, profit_percent):
    trades.append({
        'Buy Date': buy_date,
        'Buy Price': round(buy_price, 2),
        'Sell Date': sell_date,
        'Sell Price': round(sell_price, 2),
        'Profit%': round(profit_percent, 2),
        'Status': 'Closed'
    })