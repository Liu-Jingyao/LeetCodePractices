# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode_:
    def __init__(self, node=ListNode()):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        joblist = []
        import heapq
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(joblist, ListNode_(lists[i]))

        res = p = ListNode()

        while joblist:
            f = heapq.heappop(joblist).node
            p.next = f
            p = f
            if f.next:
                heapq.heappush(joblist, ListNode_(f.next))

        return res.next


def makeList(l):
    if not l:
        return None
    start = p = ListNode(l[0], None)
    if len(l) == 1:
        return start
    for i in l[1:]:
        newNode = ListNode(i, None)
        p.next = newNode
        p = p.next
    return start


def printList(l):
    while l:
        print(l.val)
        l = l.next


while True:
    s = Solution()
    lists = [makeList(l) for l in eval(input())]
    printList(s.mergeKLists(lists))
