# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        nxt = head.next if head else None

        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next if nxt else None

        return prev