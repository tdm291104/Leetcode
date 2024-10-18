class Solution:
    # Phương thức kiểm tra tính hợp lệ của chuỗi dấu ngoặc
    def isValid(self, s: str) -> bool:
        # Tạo một từ điển chứa các cặp dấu ngoặc mở và đóng tương ứng
        parentheses = {'(': ')', '{': '}', '[': ']'}
        # Khởi tạo ngăn xếp (stack) để lưu dấu ngoặc đóng cần kiểm tra
        stack = []
        # Duyệt qua từng ký tự 'b' trong chuỗi 's'
        for b in s:
            # Nếu 'b' là một dấu ngoặc mở (có trong từ điển parentheses)
            if b in parentheses:
                # Thêm dấu ngoặc đóng tương ứng vào ngăn xếp
                stack.append(parentheses[b])
            # Nếu 'b' là dấu ngoặc đóng
            # Kiểm tra ngăn xếp có rỗng hoặc dấu ngoặc không khớp với dấu ngoặc đóng mong đợi
            elif not stack or stack.pop() != b:
                # Nếu ngăn xếp rỗng hoặc dấu ngoặc không khớp, chuỗi không hợp lệ, trả về False
                return False
        # Nếu ngăn xếp không rỗng, nghĩa là còn dấu ngoặc mở chưa được đóng, trả về False
        # Ngược lại, nếu ngăn xếp rỗng, trả về True vì chuỗi hợp lệ
        return not stack

# Demo
s = Solution()
print(s.isValid("()"))  # Kết quả: True