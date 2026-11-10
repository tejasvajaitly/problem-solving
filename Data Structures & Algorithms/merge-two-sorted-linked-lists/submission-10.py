# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2 and list1.val < list2.val:
            head = list1
            extra = list2
            res = head
        elif list1 and list2 and list1.val >= list2.val:
            head = list2
            extra = list1
            res = head
        elif list1:
            return list1
        else:
            return list2
        while head and extra:
            if head.next and head.next.val < extra.val:
                head = head.next
            else:
                tmp = head.next
                head.next = extra
                extra = tmp
                head = head.next

        return res
        

