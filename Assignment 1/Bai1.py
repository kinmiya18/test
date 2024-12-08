import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Hàm tích phân
def f(x, y):
    return y + x / y**2

# Miền giới hạn của x và y
x = np.linspace(0, 2, 100)
y = np.linspace(1, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Vẽ đồ thị 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')
plt.title('Đồ thị hàm số f(x, y) = y + x/y^2')
plt.show()
