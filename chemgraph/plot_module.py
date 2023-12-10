import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import argrelextrema  # type: ignore


def plot_from_csv(file_path, save_path=None):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, delimiter=',', header=None, names=['Column1', 'Column2'])

    # Plotting
    plt.plot(df['Column1'], df['Column2'], label='Data from CSV')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Plot from CSV Data')
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

    return df


def plot_increasing_x(df, save_path=None):
    # Filter the DataFrame to include only rows where Column1 (X values) is increasing
    df_increasing_x = df[df['Column1'].diff() > 0]

    # Sort the DataFrame based on increasing X values
    df_increasing_x_sorted = df_increasing_x.sort_values(by='Column1')

    # Plotting
    plt.plot(df_increasing_x_sorted['Column1'], df_increasing_x_sorted['Column2'], label='Increasing X Data from CSV')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Plot of Increasing X Data from CSV')
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

    return df_increasing_x_sorted


def soften_plot(df, smoothing_factor, save_path=None):
    # Apply a moving average to smooth the data
    df_smoothed = df.rolling(window=smoothing_factor, min_periods=1).mean()

    # Plotting
    plt.plot(df_smoothed['Column1'], df_smoothed['Column2'],
             label=f'Smoothed Data (Factor: {smoothing_factor})')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title(f'Softened Plot (Smoothing Factor: {smoothing_factor})')
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

    return df_smoothed


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
    plt.scatter(baseline_x, baseline_y,
                label='Local Minima (Baseline)')
    plt.plot(df['Column1'], baseline_fit,
             label=f'Regression (Degree {degree})', linestyle='--')
    plt.plot(df['Column1'], df['Column2_subtracted'],
             label='Subtracted Data', linestyle='--')
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
                 fontsize=8, verticalalignment='bottom', horizontalalignment='center')

    # Plotting
    plt.plot(df['Column1'], df['Column2_subtracted'],
             label='Subtracted Data', linestyle='--')

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
