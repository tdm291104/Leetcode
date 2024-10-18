class Solution:
    # Phương thức kiểm tra xem số nguyên x có phải là số đối xứng (palindrome) hay không
    def isPalindrome(self, x: int) -> bool:
        # Nếu x là số âm, chắc chắn không phải số đối xứng, trả về False
        if x < 0:
            return False
        # Gọi hàm reverse để lấy số đảo ngược của x và so sánh với x
        # Nếu hai số bằng nhau, nghĩa là x là số đối xứng, trả về True
        return self.reverse(x) == x
    # Phương thức để đảo ngược số nguyên x
    def reverse(self, x):
        # Khởi tạo y để lưu số đảo ngược, ban đầu bằng 0
        y = 0
        # Vòng lặp thực hiện cho đến khi x bằng 0
        while x:
            # Lấy chữ số cuối cùng của x bằng phép chia dư 10
            d = x % 10
            # Thêm chữ số d vào cuối của y
            y = y * 10 + d
            # Loại bỏ chữ số cuối cùng của x bằng phép chia nguyên 10
            x //= 10
        # Trả về số đã đảo ngược
        return y

# Demo
s = Solution()
print(s.isPalindrome(121))  # Kết quả: True