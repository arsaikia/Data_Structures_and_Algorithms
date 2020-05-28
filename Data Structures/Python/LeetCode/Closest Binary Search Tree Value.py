from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def BST_from_array( array: List[int] ) :
    
    if( len(array) < 1): return None
    mid = len(array) // 2
    root = TreeNode( array[mid] )
    root.left = BST_from_array( array[ : mid] )
    root.right = BST_from_array( array[ mid+1 : ] )
    return root


def preOrderTree( node ):

    if node is None: return

    print( node.val )
    preOrderTree( node.left )
    preOrderTree( node.right )


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # while(root.left is not None):
        #     print(root)
        pass



if __name__ == "__main__":
    sol = TreeNode()
    array = [1, 2, 3, 4, 5, 6, 7] 
    array.sort()
    print(f'{array}\n')
    target = 3.714286

    preOrderTree( BST_from_array(array) )