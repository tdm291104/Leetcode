
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.preorder(p, q)

    def preorder(self, p, q):
        if not p and not q:
            return True  # Cả hai đều là None, coi như giống nhau
        if not p or not q:
            return False  # Một nút là None, nút kia không, coi như khác nhau
        if p.val != q.val:
            return False  # Các nút khác nhau, coi như khác nhau
        # Gọi đệ quy để kiểm tra các nút con bên trái và bên phải
        return self.preorder(p.left, q.left) and self.preorder(p.right, q.right)

# Demo
s = Solution()
# Tạo cây nhị phân p: [1, 2, 3]
p = TreeNode(1, TreeNode(2), TreeNode(3))
# Tạo cây nhị phân q: [1, 2, 3]
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.isSameTree(p, q))  # Kết quả: True