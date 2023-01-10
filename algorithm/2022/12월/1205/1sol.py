# leet code 876. Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        idx = 0
        while temp : 
            temp = temp.next
            idx += 1
            
        mid = idx // 2
        
        while mid : 
            head = head.next
            mid -= 1
        return head