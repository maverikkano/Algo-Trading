
# Algo Trading Project

A simple Python project using yfinance, pandas, ta, matplotlib, and backtrader.

## Structure

- `main.py`: Entry point
- `strategies/`: Custom strategies
- `utils/`: Helpers for data and plotting
- `backtests/`: Backtest scripts

## Usage
**From console:**
```bash
python main.py --symbol AAPL --start 2022-01-01 --end 2023-01-01 --interval 1d
```

**Hardcoded:**
```bash
.venv@mac 4_algo-trading-project % PYTHONPATH=. python hypothesis/RSA_EMA_v2.py
```

This also saves the image to the hypothesis folder.

## Demo
![Tesla Swing Trades](https://github.com/maverikkano/Algo-Trading/blob/main/4_algo-trading-project/artefacts/TSLA-2024.03.01-2025.04.26-1d.png)

```
.venvmaverikkano@mac 4_algo-trading-project % python main.py --symbol TSLA --start 2024-03-01 --end 2025-04-26 --interval 1d
YF.download() has changed argument auto_adjust default to True
[*********************100%***********************]  1 of 1 completed
Starting Portfolio Value: $100,000.00
Final Portfolio Value: $106,859.95
Profit% : 6.86%
Total Trades: 1
Total Profit: 109.73
Average Profit per Trade: 109.73
     Buy Date  Buy Price   Sell Date  Sell Price  Profit  Status
0  2024-04-01     175.22  2025-04-25      284.95  109.73  Closed
```