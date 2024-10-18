from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Duyệt qua danh sách nums từ đầu đến cuối
        for num in nums[0:len(nums)]:
            # Kiểm tra nếu phần tử hiện tại (num) bằng với giá trị cần loại bỏ (val)
            if num == val:
                # Nếu đúng, loại bỏ phần tử đó khỏi danh sách
                nums.remove(num)
        
        # Trả về độ dài danh sách sau khi đã loại bỏ các phần tử bằng với val
        return len(nums)

# Demo
s = Solution()
nums = [3, 2, 2, 3]
val = 3
print(s.removeElement(nums, val))  # Kết quả: 2