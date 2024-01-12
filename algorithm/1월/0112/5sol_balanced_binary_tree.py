# Leetcode 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        global flag
        flag = True

        if not root:
            return True

        def dfs(node):
            global flag
            if not flag:
                return 0

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                flag = False
                return 0

            return 1 + max(left, right)

        l = dfs(root.left)
        r = dfs(root.right)

        if not flag:
            return False

        return abs(l - r) <= 1