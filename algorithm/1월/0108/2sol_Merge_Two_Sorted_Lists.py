# Leetcode 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        now1 = list1
        now2 = list2

        temp = ListNode()

        answer = temp

        while now1 and now2:
            if now1.val < now2.val:
                temp.next = now1
                temp = now1
                now1 = now1.next
            else:
                temp.next = now2
                temp = now2
                now2 = now2.next

        if now1:
            temp.next = now1
        elif now2:
            temp.next = now2

        return answer.next