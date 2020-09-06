class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


array = [1, 2, 5, 7, 10, 13, 14, 15, 22]

def minHeightBst( array ):
    start, end = 0, len(array) - 1
    if start > end:
        return None
        
    mid = (start + end) // 2
    root = array[mid]
    lessThan = [i for i in array if i < root]
    greaterThan = [i for i in array if i > root]
    bst = BST(root)
    bst.left = minHeightBst(lessThan)
    bst.right = minHeightBst(greaterThan)
    return bst




if __name__ == "__main__":
    print(minHeightBst(array))