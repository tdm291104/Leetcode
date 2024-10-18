class Solution:
    # Phương thức chuyển đổi chuỗi chữ số La Mã sang số nguyên
    def romanToInt(self, s: str) -> int:
        # Khởi tạo biến n để lưu kết quả là số nguyên sau khi chuyển đổi
        n = 0
        # Tạo một từ điển nums chứa các cặp ký tự La Mã và giá trị tương ứng
        # Bao gồm cả các trường hợp đặc biệt (IV, IX, XL, v.v.) để xử lý dễ dàng hơn
        nums = {
            'I': 1, 'IV': 4, 'V': 5, 'VI': 6, 'IX': 9,
            'X': 10, 'XL': 40, 'L': 50, 'LX': 60,
            'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
            'DC': 600, 'CM': 900, 'M': 1000
        }
        # Vòng lặp xử lý chuỗi s cho đến khi chuỗi rỗng
        while s:
            # Lấy hai ký tự đầu tiên từ chuỗi s
            d = s[:2]
            # Cắt chuỗi s để bỏ đi hai ký tự đầu tiên (chuẩn bị cho lần lặp sau)
            s = s[2:]
            # Nếu chuỗi hai ký tự đó có trong từ điển nums
            if d in nums:
                # Thêm giá trị tương ứng vào kết quả
                n += nums[d]
            else:
                # Nếu không phải là cặp ký tự hợp lệ, chia thành từng ký tự
                d1, d2 = d[0], d[1]
                # Thêm giá trị của ký tự đầu tiên vào kết quả
                n += nums[d1]
                # Đưa ký tự thứ hai trở lại chuỗi s để xử lý trong lần lặp tiếp theo
                if d2:
                    s = d2 + s
        # Trả về kết quả sau khi chuyển đổi
        return n

# Demo
s = Solution()
print(s.romanToInt("III"))  # Kết quả: 3