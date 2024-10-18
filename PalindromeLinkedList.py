class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Phương thức kiểm tra xem danh sách liên kết có phải là palindrome không
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []  # Danh sách để lưu trữ giá trị của các nút trong danh sách liên kết
        
        # Duyệt qua danh sách liên kết và thêm giá trị của từng nút vào nums
        while head:
            nums.append(head.val)  # Thêm giá trị của nút hiện tại vào nums
            head = head.next  # Di chuyển đến nút tiếp theo
        
        # Khởi tạo hai chỉ số để kiểm tra tính đối xứng
        i = 0  # Chỉ số bắt đầu
        j = len(nums) - 1  # Chỉ số kết thúc
        
        # Kiểm tra xem các phần tử từ đầu và cuối có giống nhau không
        while i <= j:
            if nums[i] != nums[j]:  # Nếu hai phần tử không giống nhau
                return False  # Trả về False ngay lập tức
            i += 1  # Tăng chỉ số bắt đầu
            j -= 1  # Giảm chỉ số kết thúc
        
        return True  # Nếu không có sự khác biệt, trả về True

# Demo
s = Solution()
# Tạo danh sách liên kết: 1 -> 2 -> 2 -> 1
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(s.isPalindrome(head))  # Kết quả: True
# Tạo danh sách liên kết: 1 -> 2 -> 3 -> 2 -> 1
head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
print(s.isPalindrome(head))  # Kết quả: True