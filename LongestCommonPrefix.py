from typing import List

class Solution:
    # Phương thức tìm kiếm tiền tố chung dài nhất trong danh sách các chuỗi
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Nếu danh sách chuỗi rỗng, trả về chuỗi rỗng
        if not strs:
            return ''
        # Nếu danh sách chỉ có một chuỗi, trả về chính chuỗi đó vì nó là tiền tố chung duy nhất
        if len(strs) == 1:
            return strs[0]
        # Khởi tạo biến đếm i để theo dõi vị trí ký tự trong tiền tố chung
        i = 0
        # Sắp xếp danh sách chuỗi theo độ dài từ ngắn nhất đến dài nhất
        # Để đảm bảo chuỗi ngắn nhất được dùng làm tham chiếu kiểm tra
        strs = sorted(strs, key=len)
        # Lấy chuỗi ngắn nhất trong danh sách để làm tham chiếu so sánh
        word = strs[0]
        # Duyệt qua từng ký tự trong chuỗi tham chiếu
        for letter in word:
            # Gọi phương thức counter để kiểm tra xem ký tự hiện tại có xuất hiện tại cùng vị trí trong tất cả các chuỗi còn lại không
            if self.counter(strs[1:], letter, i):
                # Nếu có, tăng i để chuyển sang ký tự tiếp theo
                i += 1
            else:
                # Nếu không, kết thúc vòng lặp
                break
        # Trả về tiền tố chung dài nhất bằng cách lấy từ đầu đến vị trí i trong chuỗi tham chiếu
        return word[:i]

    # Phương thức kiểm tra ký tự tại vị trí i trong các chuỗi còn lại có giống với ký tự tham chiếu không
    def counter(self, strs, letter, i):
        # Duyệt qua từng chuỗi trong danh sách
        for word in strs:
            # Nếu ký tự tại vị trí i trong chuỗi hiện tại không giống với ký tự tham chiếu, trả về 0 (không trùng khớp)
            if letter != word[i]:
                return 0
        # Nếu tất cả chuỗi đều trùng khớp ký tự tại vị trí i, trả về 1 (trùng khớp)
        return 1

# Demo
s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # Kết quả: "fl"
