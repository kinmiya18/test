from Bai1 import volume_exact
from Bai2 import riemann_sum
import matplotlib.pyplot as plt

# Tạo danh sách các giá trị n từ 10 đến 200
n_values = range(10, 201, 10)
volumes = [riemann_sum(n) for n in n_values]

# Vẽ đồ thị
plt.plot(n_values, volumes, label='Tổng Riemann')
plt.axhline(volume_exact, color='r', linestyle='--', label='Giá trị chính xác')
plt.xlabel('Số khoảng phân hoạch (n)')
plt.ylabel('Thể tích xấp xỉ')
plt.title('Sự hội tụ của tổng Riemann')
plt.legend()
plt.grid(True)  # Thêm lưới để dễ quan sát
plt.show()
