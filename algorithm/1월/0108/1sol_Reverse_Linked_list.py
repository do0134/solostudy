# Leetcode 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head
        answer = None
        temp = None

        while now:
            temp = now.next
            now.next = answer
            answer = now
            now = temp

        return answer
