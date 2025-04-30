import os
import matplotlib.pyplot as plt
from datetime import datetime
timestamp = datetime.now().strftime("%d%m%Y%H%M%S")

def save_backtest_plot(cerebro, fileName):
    print(fileName)
    figs = cerebro.plot(style='candlestick', iplot=False)
    for i, fig in enumerate(figs):
        for f in (fig if isinstance(fig, list) else [fig]):
            filename = os.path.join(os.getcwd(), f"{fileName}-{timestamp}.png")
            f.savefig(filename, dpi=300)
            plt.close(f)