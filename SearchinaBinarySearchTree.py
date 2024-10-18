class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        if root.val > val:
            result = self.searchBST(root.left, val)
        else:
            result = self.searchBST(root.right, val)
        return result
    
# Demo
s = Solution()
# Tạo cây nhị phân [4, 2, 7, 1, 3]
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
# Tìm kiếm giá trị 2 trong cây nhị phân
result = s.searchBST(root, 2)
# In kết quả
print(result.val)  # Kết quả: 2
