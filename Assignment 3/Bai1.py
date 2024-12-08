from scipy.integrate import tplquad

# Hàm tích phân cho thể tích
def integrand(z, y, x):
    return 1  # Vì đây là tích phân thể tích, hàm là 1

# Giới hạn của z, y, và x theo thứ tự
z_lower = lambda x, y: 0
z_upper = lambda x, y: 4 - 2*x - y
y_lower = lambda x: 0
y_upper = lambda x: 4 - 2*x
x_lower = 0
x_upper = 2

# Tính thể tích bằng tích phân ba lớp
volume_exact, error = tplquad(integrand, x_lower, x_upper, y_lower, y_upper, z_lower, z_upper)
print("Thể tích tính bằng tích phân ba lớp:", volume_exact)
