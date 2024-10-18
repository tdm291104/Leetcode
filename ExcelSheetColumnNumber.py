class Solution:
    def titleToNumber(self, s: str) -> int:
        number, prod = 0, 1  # Khởi tạo số kết quả và hệ số sản phẩm
        # Duyệt chuỗi từ phải sang trái
        for char in s[::-1]:  
            # Tính giá trị cột dựa trên ký tự hiện tại
            number += (1 + ord(char) - ord('A')) * prod  
            prod *= 26  # Cập nhật hệ số sản phẩm cho ký tự tiếp theo            
        return number  # Trả về số tương ứng


# Demo
s = Solution()
print(s.titleToNumber("A"))  # Kết quả: 1