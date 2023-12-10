import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema  # type: ignore
from chemgraph.plot_module import (
    plot_from_csv,
    plot_increasing_x,
    soften_plot,
    baseline_substraction,
)


def baseline_regression_with_area(df, window_size=5, degree=1, save_path=None):
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

    # Calculate the area between y=0 and the baseline for each interval between minima
    area_list = []
    for i in range(len(minima_indices) - 1):
        start_idx = minima_indices[i]
        end_idx = minima_indices[i + 1]
        area_interval = np.trapz(np.abs(
            df['Column2_subtracted'].iloc[start_idx:end_idx]), dx=np.mean(np.diff(df['Column1'])))
        area_list.append(area_interval)

        # Display the area for each interval as a text tag
        plt.text((df['Column1'].iloc[start_idx] + df['Column1'].iloc[end_idx]) / 2,
                 0,
                 f'Area: {area_interval:.2f}',
                 fontsize=8, color='purple', verticalalignment='bottom', horizontalalignment='center')

    # Plotting
    plt.plot(df['Column1'], df['Column2_subtracted'],
             label='Subtracted Data', linestyle='--', color='blue')

    # Display the total area as a text tag
    total_area = np.sum(area_list)
    plt.text(0.5, 0.95, f'Total Area between minima: {total_area:.2f}', transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round', alpha=0.1))

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
    window_size=80
    degree=10
    df = plot_from_csv("public/blanco.csv")
    df = plot_increasing_x(df)
    df = soften_plot(df, 10)
    df = baseline_substraction(df, window_size, degree)
    df = baseline_regression_with_area(df, window_size, degree)
