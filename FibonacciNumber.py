class Solution:
    # Phương thức tính số Fibonacci thứ N
    def fib(self, N: int) -> int:
        # Khởi tạo danh sách chứa các số Fibonacci đầu tiên
        fib = [0, 1, 1]
        # Nếu N nhỏ hơn hoặc bằng 2, trả về số Fibonacci tương ứng
        if N <= 2:
            return fib[N]
        # Vòng lặp để tính các số Fibonacci tiếp theo
        while True:
            i = len(fib) - 1  # Lấy chỉ số của số Fibonacci cuối cùng hiện tại
            fib.append(fib[i] + fib[i - 1])  # Tính số Fibonacci tiếp theo
            # Kiểm tra xem đã tính đến số Fibonacci thứ N chưa
            if i == N - 1:  # Nếu đã tính đến số thứ N
                break  # Thoát khỏi vòng lặp
        # Trả về tổng của hai số Fibonacci cuối cùng (sai sót ở đây)
        return sum(fib[-3:-1])  # Trả về tổng của hai số Fibonacci cuối cùng


# Demo
s = Solution()
print(s.fib(4))  # Kết quả: 3