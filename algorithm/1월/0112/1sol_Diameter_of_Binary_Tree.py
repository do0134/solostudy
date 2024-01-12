# Leetcode 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(root):
            nonlocal answer
            if root.left:
                left = dfs(root.left)
            else:
                left = 0

            if root.right:
                right = dfs(root.right)
            else:
                right = 0

            value = 1 + max(left, right)
            answer = max(left + right, answer)

            return value

        dfs(root)

        return answer
