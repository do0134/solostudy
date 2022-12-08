# leetcode 872. Leaf-Similar Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        v1 = list()
        v2 = list()
        def dfs(root,num) :
            if not root.right and not root.left :
                if num == 1 :
                    v1.append(root.val)
                else :
                    v2.append(root.val)
                return 
            if root.right : 
                dfs(root.right,num)
            if root.left : 
                dfs(root.left,num)

        dfs(root1,1)
        dfs(root2,2)
        return v1 == v2
        