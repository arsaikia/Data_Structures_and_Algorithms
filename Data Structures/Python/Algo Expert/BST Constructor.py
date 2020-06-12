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
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BST(value)
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
