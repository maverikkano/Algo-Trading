import os
import matplotlib.pyplot as plt
from datetime import datetime
timestamp = datetime.now().strftime("%d%m%Y%H%M%S")

def save_backtest_plot(cerebro, fileName, plot_info):
    print(fileName)
    figs = cerebro.plot(style='candlestick', iplot=False)
    for i, fig in enumerate(figs):
        for f in (fig if isinstance(fig, list) else [fig]):
            f.subplots_adjust(bottom=0.25)
            metadata = str(plot_info).replace(",", "\n")
            f.text(0.02, 0.01, metadata, ha='left', va='bottom', fontsize=10, transform=f.transFigure)
            filename = os.path.join(os.getcwd(), f"{fileName}-{timestamp}.png")
            f.savefig(filename, dpi=300, bbox_inches='tight')
            plt.close(f)