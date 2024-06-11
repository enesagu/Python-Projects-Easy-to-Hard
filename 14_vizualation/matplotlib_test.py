import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.random.normal(size=1000)
y = np.random.normal(size=1000)
categories = ['A', 'B', 'C', 'D']
values = [7, 13, 5, 10]
x_line = np.linspace(0, 10, 100)
y_line = np.sin(x_line)

# Create figure and subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Histogram
axes[0, 0].hist(x, bins=30, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Histogram')
axes[0, 0].set_xlabel('Value')
axes[0, 0].set_ylabel('Frequency')

# Scatter plot
axes[0, 1].scatter(x, y, alpha=0.5)
axes[0, 1].set_title('Scatter Plot')
axes[0, 1].set_xlabel('X')
axes[0, 1].set_ylabel('Y')

# Horizontal bar chart
axes[0, 2].barh(categories, values, color='lightgreen')
axes[0, 2].set_title('Horizontal Bar Chart')
axes[0, 2].set_xlabel('Values')
axes[0, 2].set_ylabel('Categories')

# Vertical bar chart
axes[1, 0].bar(categories, values, color='lightcoral')
axes[1, 0].set_title('Vertical Bar Chart')
axes[1, 0].set_xlabel('Categories')
axes[1, 0].set_ylabel('Values')

# Line plot
axes[1, 1].plot(x_line, y_line, color='orange')
axes[1, 1].set_title('Line Plot')
axes[1, 1].set_xlabel('X')
axes[1, 1].set_ylabel('Y')

# Remove empty subplot
fig.delaxes(axes[1, 2])

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()