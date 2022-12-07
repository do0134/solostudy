# leetcode 938. Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0

        q = deque()
        q.append(root)

        while q :
            c_tree = q.popleft()
            if low <= c_tree.val <= high :
                answer += c_tree.val
            if c_tree.right != None :
                q.append(c_tree.right)
            if c_tree.left != None :
                q.append(c_tree.left)
        return answer