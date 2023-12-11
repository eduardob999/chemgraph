import matplotlib.pyplot as plt

def invert_df_y_axis_and_plot(df, save_path=None):
    inverted_df = df.copy()
    inverted_df['Column2'] = -inverted_df['Column2']

    # Plotting
    plt.plot(df['Column1'], df['Column2'], label='Original Data')
    plt.plot(inverted_df['Column1'], inverted_df['Column2'],
             label='Inverted Data', linestyle='--', color='red')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Plot with Y-axis Inverted Data')
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

    return inverted_df
