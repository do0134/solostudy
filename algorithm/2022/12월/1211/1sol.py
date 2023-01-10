# leetcode 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_v = -int(1e9)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root) :
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            single = max(max(left,right) + root.val, root.val)
            double = root.val + left + right
            value = max(root.val, single,double)

            if value > self.max_v :
                self.max_v = value
            return single
        dfs(root)
        return self.max_v
