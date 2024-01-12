# Leetcode 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/description/

class Solution:
    def __init__(self):
        self.answer = 0

    def dfs(self, node, low, high):
        if not node:
            return

        if low <= node.val <= high:
            self.answer += node.val
            self.dfs(node.right, low, high)
            self.dfs(node.left, low, high)

        if node.val > high:
            self.dfs(node.left, low, high)
        elif node.val < low:
            self.dfs(node.right, low, high)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.dfs(root, low, high)
        return self.answer