# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        first = list1
        second = list2
        if first.val <= second.val:
            current = first
            first = first.next
        else:
            current = second
            second = second.next
        res = current
        while first and second:
            if first.val <= second.val:
                current.next = first
                first = first.next
            else:
                current.next = second
                second = second.next
            current = current.next
        if not first:
            current.next = second
        elif not second:
            current.next = first
        return res