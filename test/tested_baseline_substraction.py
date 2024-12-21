import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import argrelextrema  # type: ignore

from chemgraph.plot_module import (
  soften_plot,
  plot_increasing_x
)


def baseline_substraction(df, window_size=5, degree=1, save_path=None):
    # Find local minima indices using argrelextrema
    minima_indices = argrelextrema(
        df['Column2'].values, np.less, order=window_size)[0]

    # Extract X and Y values corresponding to the local minima
    baseline_x = df['Column1'].iloc[minima_indices]
    baseline_y = df['Column2'].iloc[minima_indices]

    # Perform polynomial regression
    coeffs = np.polyfit(baseline_x, baseline_y, degree)
    baseline_fit = np.polyval(coeffs, df['Column1'])

    # Subtract the baseline fit from the original data
    df['Column2_subtracted'] = df['Column2'] - baseline_fit

    # Plotting
    plt.plot(df['Column1'], df['Column2'], label='Original Data')
    plt.scatter(baseline_x, baseline_y, color='red',
                label='Local Minima (Baseline)')
    plt.plot(df['Column1'], baseline_fit,
             label=f'Regression (Degree {degree})', linestyle='--', color='green')
    plt.plot(df['Column1'], df['Column2_subtracted'],
             label='Subtracted Data', linestyle='--', color='blue')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title(f'Plot with Baseline Regression (Degree {degree})')
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

    return df


# Example usage
if __name__ == "__main__":
    # Assuming you have a DataFrame df from some data source
    csv_file_path = 'public/blanco.csv'
    df = pd.read_csv(csv_file_path, delimiter=',',
                     header=None, names=['Column1', 'Column2'])
    df = plot_increasing_x(df)
    df = soften_plot(df, 5)
    # Set the window size for local minima detection (adjust as needed)
    window_size = 100

    # Set the degree of the polynomial regression (linear regression: degree=1)
    degree = 50

    # Plotting the original data
    plt.plot(df['Column1'], df['Column2'], label='Original Data')

    # Identify baseline from local minima and perform regression, then plot the result
    baseline_substraction(df, window_size, degree,
                        save_path='blanco_baseline_regression.png')
    plt.show()
