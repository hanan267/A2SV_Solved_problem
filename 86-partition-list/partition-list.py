# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        smaller = ListNode(0)
        greater = ListNode(0)
        small = smaller
        big = greater
        while head:
                if head.val < x:
                    small.next = head
                    small = small.next
                else:
                        big.next = head
                        big = big.next

                head = head.next
        big.next = None
        small.next = greater.next
        return smaller.next