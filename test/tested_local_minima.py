import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import argrelextrema  # type: ignore

from chemgraph.plot_module import (
  plot_from_csv,
  plot_increasing_x
)


def local_minima(df, window_size=5, save_path=None):
    # Find local minima indices using argrelextrema
    minima_indices = argrelextrema(
        df['Column2'].values, np.less, order=window_size)[0]

    # Extract X and Y values corresponding to the local minima
    baseline_x = df['Column1'].iloc[minima_indices]
    baseline_y = df['Column2'].iloc[minima_indices]

    # Plotting
    plt.plot(df['Column1'], df['Column2'], label='Original Data')
    plt.scatter(baseline_x, baseline_y, color='red',
                label='Local Minima (Baseline)')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Plot with Baseline from Local Minima')
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()


# Example usage
if __name__ == "__main__":
    # Assuming you have a DataFrame df from some data source
    csv_file_path = 'public/blanco.csv'
    df = plot_from_csv(csv_file_path)
    df = plot_increasing_x(df)

    # Set the window size for local minima detection (adjust as needed)
    window_size = 100

    # Identify baseline from local minima and plot the result
    local_minima(
        df, window_size, save_path='blanco_baseline_local_minima.png')
    plt.show()
