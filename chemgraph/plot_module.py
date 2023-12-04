import matplotlib.pyplot as plt
import pandas as pd

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

# Example usage
if __name__ == "__main__":
    csv_file_path = 'blanco.csv'
    output_image_path = 'blanco.png'
    plot_from_csv(csv_file_path, save_path=output_image_path)
