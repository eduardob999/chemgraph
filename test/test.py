from matplotlib import pyplot as plt
from chemgraph.plot_module import plot_from_csv, plot_increasing_x, soften_plot, baseline_substraction, baseline_regression_with_area

df = plot_from_csv('public/blanco.csv')

df = plot_increasing_x(df)

smoothing_factor = 10
df = soften_plot(df, smoothing_factor)

window_size = 60
degree = 10
df = baseline_substraction(df, window_size, degree)
df = baseline_regression_with_area(df, window_size, degree)
