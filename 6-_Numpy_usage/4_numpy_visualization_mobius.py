import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Mobius  paramethers
theta = np.linspace(0, 2 * np.pi, 100)
w = np.linspace(-0.25, 0.25, 8)
theta, w = np.meshgrid(theta, w)
phi = 0.5 * w

# Mobius  x, y ve z
x = (1 + w * np.cos(theta / 2)) * np.cos(phi)
y = (1 + w * np.cos(theta / 2)) * np.sin(phi)
z = w * np.sin(theta / 2)

# 3B visulation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Mobius Şeridi')

# show visualization
plt.show()
