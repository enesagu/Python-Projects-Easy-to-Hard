import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Set the style for seaborn
sns.set(style="whitegrid")

# Swarm Plot
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
sns.swarmplot(x="species", y="sepal_length", data=iris)
plt.title("Swarm Plot")

# Factor Plot (using a box plot for this example)
plt.subplot(2, 2, 2)
sns.boxplot(x="species", y="sepal_width", data=iris)
plt.title("Factor Plot (Box Plot)")

# Box Plot
plt.subplot(2, 2, 3)
sns.boxplot(x="species", y="petal_length", data=iris)
plt.title("Box Plot")

# Pair Plot
plt.subplot(2, 2, 4)
sns.pairplot(iris, hue="species", markers=["o", "s", "D"])
plt.title("Pair Plot")

# Adjust layout for better visualization
plt.tight_layout()

# Show the plots
plt.show()