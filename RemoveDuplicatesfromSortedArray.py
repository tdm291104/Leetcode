from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Duyệt qua danh sách nums từ cuối về đầu để tránh bị ảnh hưởng khi xóa phần tử
        for i in range(len(nums) - 1, 0, -1):
            # Nếu phần tử hiện tại giống với phần tử trước đó
            if nums[i] == nums[i - 1]:
                # Xóa phần tử trước đó khỏi danh sách
                nums.pop(i - 1)
    
        # Trả về độ dài danh sách sau khi đã xóa các phần tử trùng lặp
        return len(nums)
    
# Demo
s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(s.removeDuplicates(nums))  # Kết quả: 5
