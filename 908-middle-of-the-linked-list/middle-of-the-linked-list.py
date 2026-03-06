# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
         
        count = 0
        while first:
            first = first.next
            
            if count % 2 == 0:
                second = second.next
            count += 1
        return second