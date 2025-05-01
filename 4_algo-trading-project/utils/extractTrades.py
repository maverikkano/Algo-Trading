import pandas as pd

# Analytics

def extractTrades(results):
    # Access trades
    strat = results[0]  # Get the strategy instance
    trade_log = pd.DataFrame(strat.trades)

    if(trade_log.size == 0):
        return

    print("Total Trades:", len(trade_log))
    print("Total Profit:", trade_log['Profit'].sum())
    print("Average Profit per Trade:", trade_log['Profit'].mean())

    # Show the trade report
    print(trade_log)

    return trade_log