
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Phương thức kiểm tra xem hai cây nhị phân p và q có giống nhau không
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        result = []  # Danh sách để lưu kết quả kiểm tra
        self.preorder(p, q, result)  # Gọi hàm duyệt cây theo thứ tự trước
        return min(result)  # Trả về giá trị nhỏ nhất trong kết quả (True hoặc False)

    # Hàm duyệt cây theo thứ tự trước và kiểm tra sự giống nhau
    def preorder(self, p, q, result):
        if not p and not q:  # Nếu cả hai nút đều là None
            result.append(True)  # Cả hai đều là None, coi như giống nhau
            return
        if not p or not q:  # Nếu một trong hai nút là None
            result.append(False)  # Một nút là None, nút kia không, coi như khác nhau
            return
        if p.val != q.val:  # Nếu giá trị của hai nút khác nhau
            result.append(False)  # Các nút khác nhau, coi như khác nhau
        if p.val == q.val:  # Nếu giá trị của hai nút giống nhau
            result.append(True)  # Thêm True vào danh sách kết quả
            # Gọi đệ quy để kiểm tra các nút con bên trái và bên phải
            self.preorder(p.left, q.left, result)
            self.preorder(p.right, q.right, result)

# Demo
s = Solution()
# Tạo cây nhị phân p: [1, 2, 3]
p = TreeNode(1, TreeNode(2), TreeNode(3))
# Tạo cây nhị phân q: [1, 2, 3]
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.isSameTree(p, q))  # Kết quả: True