class Solution:
    # Phương thức tìm độ dài của từ cuối cùng trong chuỗi 's'
    def lengthOfLastWord(self, s: str) -> int:
        # Loại bỏ khoảng trắng thừa ở đầu và cuối chuỗi
        new_str = s.strip()
        
        # Tách chuỗi thành một danh sách các từ
        arr_str = new_str.split()
        
        # Lấy từ cuối cùng trong danh sách và trả về độ dài của nó
        return len(arr_str[len(arr_str) - 1])

# Demo
s = Solution()
print(s.lengthOfLastWord("Hello World"))  # Kết quả: 5