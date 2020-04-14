class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        
        print( self.data)

        if self.left:
            self.left.PrintTree()

        if self.right:
            self.right.PrintTree()

    def NodeDepth(self, x):

        if( x == None ): return 0

        left = 1 + self.NodeDepth(x.left) 
        right = 1 + self.NodeDepth(x.right) 

        

        return max(left, right)
         
    
    

    



if __name__ == "__main__":
    # Use the insert method to add nodes
    root = Node(4)
    root.insert(-7)
    root.insert(-3)
    root.insert(-9)
    root.insert(-3)
    root.insert(9)
    root.insert(-7)
    root.insert(-4)
    root.insert(6)
    root.insert(-6)
    root.insert(-6)
    root.insert(0)
    root.insert(6)
    root.insert(5)
    root.insert(9)
    root.insert(-1)
    root.insert(-4)
    root.insert(-2)

    

    

    #root.PrintTree()

    print((root.NodeDepth(root.left) + root.NodeDepth(root.right)))