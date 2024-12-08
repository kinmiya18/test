import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Tạo lưới cho miền D
x = np.linspace(0, 3, 100)
y1 = x**2
y2 = 3 * x

# Lưới cho miền (x, y)
X, Y = np.meshgrid(x, np.linspace(y1.min(), y2.max(), 100))
Z = X * Y

# Vẽ đồ thị
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z = xy')
plt.show()
