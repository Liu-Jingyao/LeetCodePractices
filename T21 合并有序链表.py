# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        if l1.val <= l2.val:
            res = l1
            l1 = l1.next
            locate = 1
        else:
            res = l2
            l2 = l2.next
            locate = 2

        p = res
        while l1 and l2:
            if locate == 1 and l1.val <= l2.val:
                p = l1
                l1 = l1.next
            elif locate == 1 and l1.val > l2.val:
                p.next = l2
                p = l2
                l2 = l2.next
                locate = 2
            elif locate == 2 and l2.val <= l1.val:
                p = l2
                l2 = l2.next
            elif locate == 2 and l2.val > l1.val:
                p.next = l1
                p = l1
                l1 = l1.next
                locate = 1

        if l1:
            p.next = l1
        if l2:
            p.next = l2

        return res