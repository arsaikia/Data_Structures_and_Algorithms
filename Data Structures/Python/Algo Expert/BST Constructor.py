class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

    def search(self, value):
        curr = self
        while curr is not None:
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
            else:
                return True
        return False

    def remove(self, value, parent=None):
        curr = self
        while curr is not None:
            if value < curr.value:
                parent = curr
                curr = curr.left
            elif value > curr.value:
                parent = curr
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
                elif curr == parent.left:
                    parent.left = curr.left if curr.left is not None else curr.right
                elif curr == parent.right:
                    parent.right = curr.left if curr.left is not None else curr.right
                break
        return self

    def getMinValue(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.value

    def printTree(self):
        curr = self
        if curr.left is not None:
            curr.left.printTree()
        print(str(curr.value) + " ", end='')
        if curr.right is not None:
            curr.right.printTree()


# Driver code
root = BST(12)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(5)
root.insert(13)
root.insert(22)
root.insert(1)
root.insert(14)

root.printTree()


root.remove(14)

print("\n")
root.printTree()


import math
print(math.log2(14))
