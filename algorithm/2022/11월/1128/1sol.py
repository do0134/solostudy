# Leet code Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        r_num1 = num1[::-1]
        r_num2 = num2[::-1]
        answer = int(r_num1) + int(r_num2)

        answer = str(answer)

        header = None
        linked_list = None

        for i in answer:
            if not header:
                header = ListNode(int(i))
                linked_list = header
            else:
                next_list = ListNode(int(i), linked_list)
                linked_list = next_list

        return linked_list

