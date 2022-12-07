# leetcode 938. Range Sum of BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.sum = 0
        def inorder(root):
            if not root:
                return 0
            
            if root.val >= low and root.val <= high:
               self.sum += root.val
            
            if not root.val < low:
                inorder(root.left)
            if not root.val > high:
                inorder(root.right)
            
        inorder(root)
        return self.sum