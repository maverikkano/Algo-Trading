
import matplotlib.pyplot as plt

def plot_price_and_ema(df):
    plt.figure(figsize=(20, 10))
    plt.plot(df['Close'], label='Close Price')
    if 'ema_20' in df.columns:
        plt.plot(df['ema_20'], label='EMA 20', linestyle='--')
    plt.title('Price and EMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
