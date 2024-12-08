import cv2
import numpy as np
from tensorflow.keras.models import load_model

GRID_SIZE = 9  # Kích thước lưới Sudoku (9x9)

class SudokuSolver:
    def __init__(self, model_path):
        self.board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        self.model = load_model(model_path)  # Tải mô hình CNN đã được huấn luyện

    def process_image(self, image_path):
        """Xử lý ảnh Sudoku, phân đoạn và nhận diện chữ số."""
        # Đọc ảnh và chuyển sang ảnh xám
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        _, thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)

        # Tìm lưới Sudoku qua các đường viền
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        largest_contour = max(contours, key=cv2.contourArea)
        perimeter = cv2.arcLength(largest_contour, True)
        corners = cv2.approxPolyDP(largest_contour, 0.02 * perimeter, True)

        # Biến đổi phối cảnh để chuẩn hóa lưới Sudoku
        if len(corners) == 4:
            corners = np.squeeze(corners)
            self.board = self.extract_board(image, corners)
        else:
            raise ValueError("Không thể xác định được lưới Sudoku.")

    def extract_board(self, image, corners):
        """Cắt lưới Sudoku từ ảnh gốc."""
        # Xác định góc và áp dụng biến đổi phối cảnh
        source_corners = np.array(sorted(corners, key=lambda x: (x[1], x[0])), dtype="float32")
        target_corners = np.array([[0, 0], [450, 0], [450, 450], [0, 450]], dtype="float32")
        matrix = cv2.getPerspectiveTransform(source_corners, target_corners)
        warped = cv2.warpPerspective(image, matrix, (450, 450))

        # Phân chia lưới thành 81 ô
        cells = []
        cell_size = 50
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                cell = warped[i * cell_size:(i + 1) * cell_size, j * cell_size:(j + 1) * cell_size]
                digit = self.recognize_digit(cell)
                row.append(digit)
            cells.append(row)
        return np.array(cells)

    def recognize_digit(self, cell):
        """Nhận diện chữ số trong một ô Sudoku."""
        cell = cv2.resize(cell, (28, 28))  # Chuyển kích thước về 28x28
        cell = cell.astype("float32") / 255.0  # Chuẩn hóa pixel về [0, 1]
        cell = np.expand_dims(cell, axis=-1)  # Thêm chiều kênh (channel)
        cell = np.expand_dims(cell, axis=0)  # Thêm chiều batch
        prediction = self.model.predict(cell)
        digit = np.argmax(prediction)
        return digit if np.max(prediction) > 0.8 else 0  # Trả về 0 nếu không chắc chắn

    def solve(self):
        """Giải bài toán Sudoku."""
        return self.solve_with_mrv_mac()

    def solve_with_mrv_mac(self):
        """Giải Sudoku với heuristic MRV và duy trì tính nhất quán cung MAC."""
        row, col = self.get_mrv_cell()  # Chọn ô có ít giá trị khả dĩ nhất
        if row is None:
            return True  # Hoàn tất giải Sudoku

        for num in range(1, GRID_SIZE + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve_with_mrv_mac():
                    return True
                self.board[row][col] = 0  # Quay lui
        return False

    def get_mrv_cell(self):
        """Tìm ô có miền giá trị nhỏ nhất (MRV)."""
        min_options = GRID_SIZE + 1
        best_cell = None

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.board[row][col] == 0:
                    options = self.get_valid_numbers(row, col)
                    if len(options) < min_options:
                        min_options = len(options)
                        best_cell = (row, col)
        return best_cell

    def get_valid_numbers(self, row, col):
        """Lấy các giá trị hợp lệ cho một ô."""
        valid_numbers = set(range(1, GRID_SIZE + 1))

        # Kiểm tra hàng, cột và ô vuông con
        valid_numbers -= set(self.board[row, :])
        valid_numbers -= set(self.board[:, col])
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        valid_numbers -= set(self.board[start_row:start_row + 3, start_col:start_col + 3].flatten())
        return valid_numbers

    def is_valid(self, row, col, num):
        """Kiểm tra số num có hợp lệ tại ô (row, col)."""
        return (
            num not in self.board[row, :] and
            num not in self.board[:, col] and
            num not in self.board[3 * (row // 3):3 * (row // 3) + 3, 3 * (col // 3):3 * (col // 3) + 3]
        )

    def print_board(self):
        """In lưới Sudoku."""
        for row in self.board:
            print(" ".join(str(num) if num != 0 else "." for num in row))


# Chạy chương trình
if __name__ == "__main__":
    solver = SudokuSolver("digit_model.h5")  # Đường dẫn tới mô hình CNN
    solver.process_image("./sudoku.jpg")  
    print("Bảng Sudoku ban đầu:")
    solver.print_board()

    if solver.solve():
        print("\nBảng Sudoku sau khi giải:")
        solver.print_board()
    else:
        print("\nKhông tìm được lời giải cho bài toán Sudoku.")
