class Solution:
    # Phương thức cộng hai chuỗi nhị phân và trả về kết quả dưới dạng chuỗi nhị phân
    def addBinary(self, a: str, b: str) -> str:
        # Đảo ngược chuỗi và chuyển thành danh sách
        a = list(a[::-1])
        b = list(b[::-1])
        
        # Lấy độ dài của hai chuỗi
        length_a = len(a)
        length_b = len(b)
        
        # Biến tạm để lưu giá trị carry
        temp = '0'
        i = 0
        
        # Đảm bảo hai danh sách có cùng độ dài
        if length_a < length_b: 
            a += ['0'] * (length_b - length_a)  # Thêm 0 vào cuối danh sách a
            length_a = len(a)
        else: 
            b += ['0'] * (length_a - length_b)  # Thêm 0 vào cuối danh sách b

        # Vòng lặp để thực hiện phép cộng
        while True:
            # Tính tổng của các chữ số và carry
            total = int(a[i]) + int(b[i]) + int(temp)
            
            # Xử lý các trường hợp của tổng
            if total == 3:  # 1 + 1 + 1
                a[i] = '1'
                temp = '1'  # C carry
            elif total == 2:  # 1 + 1 + 0 hoặc 0 + 0 + 1
                a[i] = '0'
                temp = '1'  # C carry
            elif total == 1:  # 1 + 0 + 0 hoặc 0 + 1 + 0
                a[i] = '1'
                temp = '0'  # Không có carry
            else:  # 0 + 0 + 0
                a[i] = '0'
                temp = '0'  # Không có carry
            
            i += 1
            
            # Nếu đã đến cuối danh sách và còn carry
            if i == length_a and temp == '1':
                a.append(temp)  # Thêm 1 vào cuối danh sách
                break
            
            # Nếu đã đến cuối danh sách mà không còn carry
            if i == length_a:
                break
        
        # Đảo ngược lại danh sách và chuyển thành chuỗi để trả về
        return ''.join(a[::-1])


# Demo
s = Solution()
print(s.addBinary("11", "1"))  # Kết quả: "100"