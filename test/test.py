from matplotlib import pyplot as plt
from chemgraph.plot_module import invert_y_axis, plot_from_csv, plot_increasing_x, soften_plot, baseline_substraction, baseline_regression_with_area

df = plot_from_csv('public/blanco.csv')
df = invert_y_axis(df)

df = plot_increasing_x(df, decreasing=True)

smoothing_factor = 10
df = soften_plot(df, smoothing_factor)

window_size = 10
degree = 3
df = baseline_substraction(df, window_size, degree)
df = baseline_regression_with_area(df, window_size, degree)
