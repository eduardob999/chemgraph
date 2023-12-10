import matplotlib.pyplot as plt
import pandas as pd


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


# Example usage
if __name__ == "__main__":
    csv_file_path = 'public/blanco.csv'
    output_image_path = 'blanco_sorted_increasing_x.png'
    df = pd.read_csv(csv_file_path, delimiter=',',
                     header=None, names=['Column1', 'Column2'])

    # Soften the plot
    soften_plot(df, smoothing_factor=10, save_path='blanco_softened.png')
