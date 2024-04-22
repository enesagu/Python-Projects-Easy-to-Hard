import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function for 3D Data Visualization
def visualize_3d_data():
    # Generate sample data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    # 3D Visualization
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Surface plot
    surf = ax.plot_surface(x, y, z, cmap='viridis')
    fig.colorbar(surf)

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Add title
    plt.title('3D Data Visualization')
    
    # Show the plot
    plt.show()

# Function for 4D Data Visualization
def visualize_4d_data():
    # Generate sample data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    z = np.linspace(-5, 5, 100)
    t = np.linspace(0, 10, 100)
    x, y, z, t = np.meshgrid(x, y, z, t)
    w = np.sin(np.sqrt(x**2 + y**2 + z**2 + t**2))

    # 4D Visualization
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot
    surf = ax.scatter(x, y, z, c=t, cmap='viridis')
    fig.colorbar(surf)

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Add title
    plt.title('4D Data Visualization')
    
    # Show the plot
    plt.show()

# Main function
def main():
    # Visualize 3D data
    print("3D Data Visualization:")
    visualize_3d_data()
    
    # Visualize 4D data
    print("4D Data Visualization:")
    visualize_4d_data()

if __name__ == "__main__":
    main()
