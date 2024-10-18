from typing import List

class Solution:
    # Phương thức tìm các từ có thể gõ chỉ bằng một hàng phím
    def findWords(self, words: List[str]) -> List[str]:
        # Định nghĩa ba hàng phím trên bàn phím QWERTY
        first_row = "qwertyuiopQWERTYUIOP"
        second_row = "asdfghjklASDFGHJKL"
        third_row = "zxcvbnmZXCVBNM"
        result = []  # Danh sách để lưu các từ hợp lệ
        # Duyệt qua từng từ trong danh sách 'words'
        for word in words:
            # Sử dụng phương thức strip để loại bỏ các ký tự trong các hàng phím
            t1 = word.strip(first_row)  # Loại bỏ ký tự từ hàng đầu
            t2 = word.strip(second_row)  # Loại bỏ ký tự từ hàng giữa
            t3 = word.strip(third_row)  # Loại bỏ ký tự từ hàng dưới
            # Kiểm tra xem từ có thể gõ bằng một hàng nào không
            if(t1 == "" or t2 == "" or t3 == ""):
                result.append(word)  # Nếu có thể, thêm từ vào danh sách kết quả        
        return result  # Trả về danh sách các từ hợp lệ


# Demo
s = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]
print(s.findWords(words))  # ["Alaska", "Dad"]