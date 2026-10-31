# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = second = 0
        list1 = l1
        list2 = l2
        n = m = 0
        while list1:
            first += list1.val*10**n
            list1 = list1.next
            n += 1
        while list2:
            second += list2.val*10**m
            list2 = list2.next
            m += 1
        res = first + second
        new = ListNode(res%10)
        res = res//10

        current = new
        while res:
            current.next = ListNode(res%10)
            current = current.next  
            res = res//10
        return new