from typing import List

class Solution:
    # Phương thức hợp nhất hai danh sách đã sắp xếp nums1 và nums2
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: 
        # Gán các phần tử của nums2 vào phần cuối của nums1, bắt đầu từ vị trí m
        nums1[m:] = nums2
        
        # Sắp xếp lại nums1 sau khi thêm các phần tử từ nums2
        nums1.sort()

# Demo 
s = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)  # Kết quả: [1, 2, 2, 3, 5, 6]
