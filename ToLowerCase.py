class Solution:
    # Phương thức chuyển đổi tất cả các ký tự trong chuỗi 's' thành chữ thường
    def toLowerCase(self, s: str) -> str:
        ans = ''  # Khởi tạo một chuỗi rỗng để lưu kết quả
        
        # Duyệt qua từng ký tự trong chuỗi 's'
        for c in s:
            # Kiểm tra xem ký tự 'c' có phải là chữ hoa không (A-Z)
            if ord(c) in range(65, 91):  # ASCII của 'A' là 65 và 'Z' là 90
                # Nếu là chữ hoa, chuyển đổi sang chữ thường bằng cách cộng 32
                ans += chr(ord(c) + 32)  # Chuyển đổi và thêm vào 'ans'
            else:
                ans += c  # Nếu không phải chữ hoa, thêm ký tự gốc vào 'ans'
        
        return ans  # Trả về chuỗi kết quả

# Demo
s = Solution()
print(s.toLowerCase("Hello"))  # Kết quả: "hello"