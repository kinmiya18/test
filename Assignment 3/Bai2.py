def riemann_sum(n):
    dx = 2 / n
    dy = 4 / (2 * n)
    dz = 4 / (3 * n)
    volume_approx = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x = i * dx
                y = j * dy
                z = k * dz
                if 2 * x + y + z <= 4:  # Điều kiện để điểm (x, y, z) nằm trong khối tứ diện
                    volume_approx += dx * dy * dz
    return volume_approx

volume_approx_n50 = riemann_sum(50)
print("Thể tích tính bằng tổng Riemann với n=50:", volume_approx_n50)
