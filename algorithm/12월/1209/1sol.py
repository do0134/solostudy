# leetcode 1026. Maximum Difference Between Node and Ancestor
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_v = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(root, ma, mi) :
            if root.val > ma :
                ma = root.val
                if ma != -1 and mi != int(1e9) :
                    if self.max_v < abs(ma - mi) :
                        self.max_v = abs(ma-mi)
            if root.val < mi :
                mi = root.val
                if ma != -1 and mi != int(1e9) :
                    if self.max_v < abs(ma - mi) :
                        self.max_v = abs(ma-mi)
            
            if root.right : 
                dfs(root.right,ma,mi)
            if root.left : 
                dfs(root.left,ma,mi)
        dfs(root,-1,int(1e9))
        return self.max_v
    max_v = 0

