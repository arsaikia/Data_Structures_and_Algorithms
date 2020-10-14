# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        intersect = self.hasCycle(slow, fast)
        if intersect is None:
            return None
        p1, p2 = head, intersect
        while p1 != p2:
            p1, p2 = p1.next, p2.next
        return p1

    def hasCycle(self, slow: ListNode, fast: ListNode) -> ListNode:
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return fast
        return None
    
