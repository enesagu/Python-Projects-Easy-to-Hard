from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
import numpy as np

# Output to notebook
output_notebook()

# Create data
x = np.linspace(0, 4*np.pi, 100)
y_line = np.sin(x)
y_cos = np.cos(x)
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 2]
x_scatter = np.random.rand(50) * 10
y_scatter = np.random.rand(50) * 10

# Line plot
line_plot = figure(title="Line Plot", x_axis_label='x', y_axis_label='sin(x)')
line_plot.line(x, y_line, line_width=2)

# Cosine plot
cos_plot = figure(title="Cosine Plot", x_axis_label='x', y_axis_label='cos(x)')
cos_plot.line(x, y_cos, line_color="red", line_width=2)

# Bar chart
bar_chart = figure(x_range=categories, title="Bar Chart", x_axis_label='Categories', y_axis_label='Values')
bar_chart.vbar(x=categories, top=values, width=0.5)

# Scatter plot
scatter_plot = figure(title="Scatter Plot", x_axis_label='x', y_axis_label='y')
scatter_plot.scatter(x_scatter, y_scatter, size=8, color="navy", alpha=0.5)

# Show plots
show(line_plot)
show(cos_plot)
show(bar_chart)
show(scatter_plot)