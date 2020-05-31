# Definition for singly-linked list.

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        
        Node = head
        if(Node.next == None):
            return head if Node.val != val else None
        
        while Node.next is not None:
            nodeToRemove = Node
            Node = Node.next
            if nodeToRemove.next.val == val:
                self.removeBindings(nodeToRemove)
        
        return head

        def removeBindings(self, Node):
            nodeToRemove = Node.next
            Node.next = nodeToRemove.next


