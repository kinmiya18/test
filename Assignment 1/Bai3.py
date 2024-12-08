def f(x, y):
    return y + x / y**2
def riemann_sum(f, a, b, c, d, n):
    dx = (b - a) / n
    dy = (d - c) / n
    total_sum = 0

    for i in range(n):
        for j in range(n):
            x = a + (i + 0.5) * dx
            y = c + (j + 0.5) * dy
            total_sum += f(x, y) * dx * dy

    return total_sum

# Tính tổng Riemann với n=50
result_riemann = riemann_sum(f, 0, 2, 1, 2, 50)
print("Kết quả tổng Riemann với n=50: ", result_riemann)
