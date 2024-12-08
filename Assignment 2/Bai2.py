from scipy.integrate import dblquad

# Định nghĩa hàm f(x, y) = x * y
def f(x, y):
    return x * y

# Tính tích phân trên miền D
I, error = dblquad(f, 0, 3, lambda x: x**2, lambda x: 3 * x)

print(f"Tích phân: {I}, Sai số: {error}")
