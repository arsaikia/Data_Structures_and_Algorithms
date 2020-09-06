# from binarytree import Node

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # O(n) Time | O(n) Space
    def printTree(self):
        curr = self
        if curr is None:
            return

        else:
            if curr.left is not None:
                curr.left.printTree()
            if curr.right is not None:
                curr.right.printTree()
        print(curr.value)

    # Average: O(log(n)) Time | O(log(n)) Space
    # Worst: O(n) Time | O(n) Space
    def insert(self, value):
        curr = self
        while True:
            if value < curr.value:
                if curr.left is None:
                    curr.left = BST(value)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BST(value)
                    break
                else:
                    curr = curr.right
        return self

    # Average: O(log(n)) Time | O(log(n)) Space
    # Worst: O(n) Time | O(n) Space
    def contains(self, value):
        curr = self
        while curr is not None:
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
            else:
                return True
        return False

    # Average: O(log(n)) Time | O(log(n)) Space
    # Worst: O(n) Time | O(n) Space
    def remove(self, value, parent=None):
        curr = self
        while curr is not None:
            if value < curr.value:
                parent = curr
                curr = curr.left
            elif value > curr.value:
                parent = curr.value
                curr = curr.right
            else:
                if curr.left is not None and curr.right is not None:
                    curr.value = curr.right.getMinValue()
                    curr.right.remove(curr.value, curr)
                elif parent is None:
                    if curr.left is not None:
                        curr.value = curr.left.value
                        curr.right = curr.left.right
                        curr.left = curr.left.left
                    elif curr.right is not None:
                        curr.value = curr.right.value
                        curr.left = curr.right.left
                        curr.right = curr.right.right
                    else:
                        curr = None
                elif parent.left is curr:
                    parent.left = curr.left if curr.left is not None else curr.right
                elif parent.right is curr:
                    parent.right = curr.left if curr.left is not None else curr.right
                break
        return curr

    # Average: O(log(n)) Time | O(log(n)) Space
    # Worst: O(n) Time | O(n) Space
    def getMinValue(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.value


if __name__ == "__main__":
    bst = BST(10)
    bst.insert(30).insert(5).insert(2).insert(12).insert(20)
    bst.printTree()
    print(bst.contains(12))
    bst.remove(12)
    print("\n")
    bst.printTree()
