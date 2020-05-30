import copy 

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList( head ):
    headPt1 = head
    i = 1
    while headPt1.next:
        print(f'Node {i} value : {headPt1.val}')
        headPt1 = headPt1.next
        i += 1
    return None

def reverseLinkedList( head ):
    prev, curr = None, head
    while curr :
        curr.next, prev, curr = prev, curr, curr.next
    return prev

def createList( array ):

    head = Node(array[0])
    curr = copy.deepcopy(head)
    for i in range(1, len(array)):
        curr = curr.next
        curr = Node(array[i])
        
    
    return curr



if __name__ == "__main__":
    
    array = [1,2,3,4,5]

    
    # print(head.val, head.next.val)
    print(f'\nThe values of the Linked List are :')

    printList( createList( array ) )

    # printList( reverseLinkedList( head ) )
    