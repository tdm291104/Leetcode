from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Duyệt qua từng phần tử trong danh sách nums cùng với chỉ số của nó
        for i, n in enumerate(nums):
            # Kiểm tra xem số đó có xuất hiện trong phần còn lại của danh sách hay không
            if target-n in nums[i+1:]:
                # Nếu có, trả về chỉ số của n và chỉ số của số cần tìm
                return i, i+1+nums[i+1:].index(target-n)

# Demo
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  # Kết quả: (0, 1)