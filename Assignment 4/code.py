import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Bước 1: Xác định trường vector F và đường cong C
def F(x, y, z):
    """Vector field F(x, y, z) = xi + yj + zk"""
    return np.array([x, y, z])

def r(t):
    """Parametrized curve r(t) = t*i + t^2*j + t^3*k"""
    x = t
    y = t**2
    z = t**3
    return np.array([x, y, z])

# Bước 2: Vẽ trường vector trong không gian 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Tạo grid trong không gian 3D
x, y, z = np.linspace(-1, 1, 5), np.linspace(-1, 1, 5), np.linspace(-1, 1, 5)
X, Y, Z = np.meshgrid(x, y, z)

# Tính các thành phần của trường vector tại các điểm
U = X
V = Y
W = Z

# Vẽ các vector
ax.quiver(X, Y, Z, U, V, W, length=0.1, normalize=True, color="blue")

# # Bước 3: Vẽ đường cong C lên hình
# t_vals = np.linspace(0, 1, 100)
# curve = np.array([r(t) for t in t_vals])
# ax.plot(curve[:, 0], curve[:, 1], curve[:, 2], color="red", linewidth=2, label="Curve C: r(t)")

# Định dạng đồ thị
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Vector Field and Curve C")
ax.legend()
plt.show()

# Bước 4: Tính tích phân đường
def integrand(t):
    """Tích phân đường: F . dr/dt"""
    r_t = r(t)
    dr_dt = np.array([1, 2*t, 3*t**2])  # Derivative of r(t) = [1, 2t, 3t^2]
    return np.dot(F(*r_t), dr_dt)

result, _ = quad(integrand, 0, 1)
print(f"Kết quả tích phân đường: {result}")
