# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        slowPtr = fastPtr = head
        position = 1

        while fastPtr is not None and position <= n:
            fastPtr = fastPtr.next
            position += 1

        if fastPtr is None:
            head = head.next
            return head

        while fastPtr.next is not None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next

        slowPtr.next = slowPtr.next.next

        return head
