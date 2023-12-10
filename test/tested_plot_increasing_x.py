import matplotlib.pyplot as plt
import pandas as pd

def plot_increasing_x(file_path, save_path=None):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, delimiter=',', header=None, names=['Column1', 'Column2'])

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

# Example usage
if __name__ == "__main__":
    csv_file_path = 'public/blanco.csv'
    output_image_path = 'blanco_sorted_increasing_x.png'
    plot_increasing_x(csv_file_path, save_path=output_image_path)
