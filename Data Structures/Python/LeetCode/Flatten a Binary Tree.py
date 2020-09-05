from binarytree import Node







if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.left.left = Node(3)
    tree.left.right = Node(4)
    tree.right = Node(5)
    tree.right.right = Node(6)
    print(tree)
