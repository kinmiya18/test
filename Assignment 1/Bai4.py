import matplotlib.pyplot as plt

n_values = range(10, 201, 10)
riemann_values = []
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
for n in n_values:
    
    riemann_values.append(riemann_sum(f, 0, 2, 1, 2, n))

plt.plot(n_values, riemann_values)
plt.xlabel('Số khoảng phân hoạch n')
plt.ylabel('Giá trị tổng Riemann')
plt.title('Sự hội tụ của tổng Riemann')
plt.show()
