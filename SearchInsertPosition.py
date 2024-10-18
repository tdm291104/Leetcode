from typing import List

class Solution:
    # Phương thức tìm vị trí chèn của 'target' trong danh sách đã sắp xếp 'nums'
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Khởi tạo biến con trỏ bên trái (l) và bên phải (r)
        l = 0
        r = len(nums) - 1
        # Thực hiện tìm kiếm nhị phân
        while l <= r:
            # Tính toán chỉ số giữa (m) giữa l và r
            m = (l + r) // 2
            # Nếu m là chỉ số cuối và target lớn hơn giá trị tại nums[m], trả về m+1
            if m == r and target > nums[m]:
                return m + 1
            # Nếu target lớn hơn giá trị tại nums[m], dịch con trỏ trái (l) sang bên phải
            if target > nums[m]:
                l = m + 1
            else:
                # Nếu target nhỏ hơn hoặc bằng giá trị tại nums[m], dịch con trỏ phải (r) sang bên trái
                r = m - 1
        # Trả về m là vị trí tìm được, nhưng có thể không đúng trong một số trường hợp cần cải thiện
        return m

# Demo
s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))  # Kết quả: 2