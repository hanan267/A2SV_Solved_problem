# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # dummy = ListNode(None)
        # dummy.next = head
        # head = dummy

        # if head == None:
        #     return 
        # # def 
        # current = head
        # while current.next:
        #     prev = current
        #     current = current.next
        #     if current.val == val:
        #         prev.next = current.next
        #         current = prev
        #         # num.next = None
        # return head.next


        dummy = ListNode(None)
        dummy.next =  head
        head = dummy
        if head.next == None:
            return
        current = head
        while current.next:
            prev = current
            current = current.next
            if current.val == val:
                prev.next = current.next
                current = prev
                
        return head.next

                




























        