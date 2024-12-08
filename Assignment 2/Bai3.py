# Hàm tính tổng Riemann
def f(x, y):
    return x * y

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

# Số khoảng phân hoạch n = 50
n = 50
riemann_result = riemann_sum(f, 0, 3, n)
print(f"Tổng Riemann với n=50: {riemann_result}")
