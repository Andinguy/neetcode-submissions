# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = ListNode(0,head)
        curr = dummy
        while head:
            length +=1
            head = head.next
        toRemove = length - n

        for i in range(toRemove):
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next
        

        