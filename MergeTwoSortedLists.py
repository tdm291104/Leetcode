class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Phương thức trộn hai danh sách liên kết đã được sắp xếp (tăng dần) thành một danh sách liên kết mới
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Tạo biến con trỏ để duyệt qua các node của l1 và l2
        node1 = l1
        node2 = l2
        
        # Tạo một danh sách liên kết mới, với node đầu tiên là một node giả (dummy node)
        l3 = ListNode()
        node = l3
        
        # Duyệt qua l1 và l2 cho đến khi tất cả các node được hợp nhất
        while node:
            # Nếu cả node1 và node2 còn node và node1 có giá trị lớn hơn node2
            if node1 and node2 and node1.val > node2.val:
                # Thêm node của l2 (node2) vào danh sách kết quả (l3)
                node.next = node2
                # Di chuyển đến node tiếp theo trong l2
                node2 = node2.next
            
            # Nếu chỉ còn lại node trong l1
            elif node1:
                # Thêm node của l1 vào danh sách kết quả
                node.next = node1
                # Di chuyển đến node tiếp theo trong l1
                node1 = node1.next
            
            # Nếu chỉ còn lại node trong l2
            elif node2:
                # Thêm node của l2 vào danh sách kết quả
                node.next = node2
                # Di chuyển đến node tiếp theo trong l2
                node2 = node2.next
            
            # Di chuyển đến node tiếp theo trong danh sách kết quả (l3)
            node = node.next
        
        # Trả về danh sách liên kết đã được trộn, bắt đầu từ node tiếp theo của node giả
        return l3.next

# Demo
s = Solution()
# Tạo danh sách liên kết l1: 1 -> 2 -> 4
l1 = ListNode(1, ListNode(2, ListNode(4)))
# Tạo danh sách liên kết l2: 1 -> 3 -> 4
l2 = ListNode(1, ListNode(3, ListNode(4)))
# Trộn hai danh sách liên kết l1 và l2
result = s.mergeTwoLists(l1, l2)
# In kết quả
while result:
    print(result.val, end=' ')
    result = result.next
# Kết quả: 1 1 2 3 4 4