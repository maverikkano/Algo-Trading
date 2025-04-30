import argparse
from backtests.run_backtest import run_backtest

def main():
    parser = argparse.ArgumentParser(description="Algo Trading Strategy Runner")
    parser.add_argument('--symbol', type=str, default="AAPL", help="Stock symbol")
    parser.add_argument('--start', type=str, default="2022-01-01", help="Start date")
    parser.add_argument('--end', type=str, default="2023-01-01", help="End date")
    parser.add_argument('--interval', type=str, default="1d", help="Interval")
    
    args = parser.parse_args()

    run_backtest(symbol=args.symbol, start=args.start, end=args.end, interval=args.interval, strategy="Rsi_ema_v2")

if __name__ == "__main__":
    main()
