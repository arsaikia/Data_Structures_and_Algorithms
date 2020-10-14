from binarytree import Node


def flatten( node ):
    if node is None:
        return None
    if node.left is None and node.right is None:
        return node
    left = flatten(node.left)
    right = flatten(node.right)
    
    if left:
        left.right = node.right
        node.right = node.left
        node.left = None
    return right if right is not None else left
    





if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.left.left = Node(3)
    tree.left.right = Node(4)
    tree.right = Node(5)
    tree.right.right = Node(6)
    print(tree)
    
    flatten(tree)
    node = tree
    
    while node:
        print(node.val)
        node = node.right
    
