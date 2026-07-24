# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = ListNode(0,head)
        curr1 = head
        curr2 = dummy
        while curr1:
            count +=1
            curr1 = curr1.next
        count -= n
        for i in range((count)):
            count -=1
            curr2 = curr2.next
        curr2.next = curr2.next.next

        return dummy.next