# leetcode 328. Odd Even Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None : 
            return head
        
        idx = 1

        oddNode = ListNode()
        evenNode = ListNode()
        odd = oddNode
        even = evenNode

        while head != None :
            if idx == 1 :
                odd.next = head
                odd = odd.next
                idx = 2
            else : 
                even.next = head
                even = even.next
                idx = 1
            head = head.next

        odd.next = evenNode.next
        even.next = None
        return oddNode.next               
