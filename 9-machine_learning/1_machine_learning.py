import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)  # Set seed for reproducibility
X = np.random.rand(100, 1)  # Generate random input values
y = 2 * X.squeeze() + np.random.randn(100)  # Generate output values with noise

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()  # Create a linear regression model
model.fit(X_train, y_train)  # Fit the model to the training data

# Evaluate the model
train_score = model.score(X_train, y_train)  # Calculate the R^2 score on the training data
test_score = model.score(X_test, y_test)  # Calculate the R^2 score on the testing data

# Print evaluation results
print("Training R^2 score:", train_score)
print("Testing R^2 score:", test_score)

# Plot the data points and the regression line
plt.scatter(X, y, color='blue', label='Data Points')  # Plot the data points
plt.plot(X, model.predict(X), color='red', label='Regression Line')  # Plot the regression line
plt.xlabel('X')  # Set label for x-axis
plt.ylabel('y')  # Set label for y-axis
plt.title('Linear Regression')  # Set title for the plot
plt.legend()  # Display legend
plt.show()  # Show the plot
