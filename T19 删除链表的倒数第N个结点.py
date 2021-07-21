# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        llen = 0
        p = head
        a = [head]
        while(p.next):
            p = p.next
            llen += 1
            a.append(p)
        if llen-n+1 == 0:
            head = head.next
        else:
            pdp = a[llen-n]
            pdp.next = pdp.next.next
        return head

