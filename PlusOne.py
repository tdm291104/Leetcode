from typing import List

class Solution:
    # Phương thức cộng thêm 1 vào số được biểu diễn dưới dạng danh sách các chữ số
    def plusOne(self, digits: List[int]) -> List[int]:
        d = 0  # Khởi tạo biến d để lưu trữ giá trị số nguyên
        l = len(digits)  # Lấy độ dài của danh sách digits
        
        # Chuyển đổi danh sách chữ số thành số nguyên
        for digit in digits:
            d = d * 10 + digit  # Xây dựng số nguyên từ danh sách chữ số
        
        d += 1  # Cộng thêm 1 vào số nguyên
        
        digits.clear()  # Xóa danh sách digits để chuẩn bị lưu trữ kết quả mới
        
        # Chuyển đổi số nguyên d trở lại thành danh sách các chữ số
        while d:
            number = d % 10  # Lấy chữ số cuối cùng
            digits.insert(0, number)  # Chèn chữ số vào đầu danh sách
            d //= 10  # Chia d cho 10 để loại bỏ chữ số cuối cùng
        
        # Nếu độ dài danh sách digits nhỏ hơn l, thêm các số 0 vào đầu
        while len(digits) < l:
            digits.insert(0, 0)
        
        return digits  # Trả về danh sách kết quả

# Demo
s = Solution()
print(s.plusOne([1, 2, 3]))  # Kết quả: [1, 2, 4]