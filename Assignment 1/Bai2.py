import scipy.integrate as integrate

# Hàm tích phân
def f(x, y):
    return y + x / y**2

# Tính tích phân với SciPy
result = integrate.dblquad(f, 0, 2, lambda x: 1, lambda x: 2)
print("Kết quả tích phân chính xác: ", result[0])
