# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        root = ListNode(-1)
        head = root
        
        head1 = l1
        head2 = l2
        
        while(head1 and head2):
            
            if(head1.val < head2.val):
                head.next = head1
                head1 = head1.next
                
            else:
                head.next = head2
                head2 = head2.next
                
            head = head.next
            
        head.next = head1 or head2
            
        return root.next
        