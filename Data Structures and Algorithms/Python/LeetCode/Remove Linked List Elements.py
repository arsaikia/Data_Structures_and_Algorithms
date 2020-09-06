# Definition for singly-linked list.

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        while(head is not None and head.val == val):
            head = head.next
        if head == None:
            return head

        Node = head
        while Node.next is not None:
            nodeToRemove = Node.next
            if nodeToRemove.val == val:
                Node.next = nodeToRemove.next
            else:
                Node = Node.next

        return head
