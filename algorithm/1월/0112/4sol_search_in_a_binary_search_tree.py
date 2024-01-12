# Leetcode 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return

        q = deque()
        q.append(root)

        while q:
            now_node = q.popleft()
            if not now_node:
                continue

            if now_node.val == val:
                return now_node

            q.append(now_node.left)
            q.append(now_node.right)

        return