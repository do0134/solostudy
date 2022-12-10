# leetcode 1339. Maximum Product of Splitted Binary Tree
# preorder를 쓴 다음, sum_list인자를 total//2에 뺀 값으로 대입하면 보다 시간을 줄일 수 있을듯 하다.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sum_set = set()
        max_v = 0

        def dfs(node) :
            if not node : 
                return 0
            
            if not node.left and not node.right : 
                sum_set.add(node.val)
                return node.val

            else :
                value = dfs(node.left) + dfs(node.right) + node.val
                sum_set.add(value)
                return value
        
        total = dfs(root)
        sum_list = list(sum_set)

        for i in sum_list :
            max_v = max(max_v, i*(total-i))
        
        return max_v % (10**9 + 7)