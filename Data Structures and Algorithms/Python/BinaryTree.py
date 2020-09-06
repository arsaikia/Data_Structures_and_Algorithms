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

    def getMaxDia(self, root):

        self.x = 0
        self.diameter(root)
        return self.x

         
    def diameter( self, root):

        if not root: return 0

        L = self.diameter(root.left)
        R= self.diameter(root.right)
         
        total = L+R+1

        self.x =  max( self.x, total)

        return 1+max(L,R)

        

    
    

    



if __name__ == "__main__":
    # Use the insert method to add nodes
    y = [1,2,3,4,5]
    root = Node(1)
    for i in range(1, len(y)):
        root.insert(i)

    

    

    #root.PrintTree()

    print((root.getMaxDia(root)))