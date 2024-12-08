import matplotlib.pyplot as plt
from scipy.integrate import dblquad


def f(x, y):
    return x * y
I, error = dblquad(f, 0, 3, lambda x: x**2, lambda x: 3 * x)

# Giá trị tích phân chính xác
exact_value = I
def riemann_sum(f, x_min, x_max, n):
    dx = (x_max - x_min) / n
    total_sum = 0
    for i in range(n):
        x = x_min + i * dx
        y_min = x**2
        y_max = 3 * x
        dy = (y_max - y_min) / n
        for j in range(n):
            y = y_min + j * dy
            total_sum += f(x, y) * dx * dy
    return total_sum

# Danh sách các giá trị của n
n_values = list(range(10, 201, 10))
riemann_values = [riemann_sum(f, 0, 3, n) for n in n_values]

# Vẽ đồ thị
plt.plot(n_values, riemann_values, label='Tổng Riemann')
plt.axhline(y=exact_value, color='r', linestyle='--', label='Giá trị chính xác')
plt.xlabel('Số khoảng phân hoạch (n)')
plt.ylabel('Giá trị tổng Riemann')
plt.legend()
plt.title('Sự hội tụ của tổng Riemann tới giá trị chính xác')
plt.show()
