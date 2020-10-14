class Node:
    def __init__(self, val=0):
        self.val = val
        self.children = []

    def addChild(self, val):
        self.children.append(Node(val))
        return self

    def depthFirstSearch(self, arr):
        arr.append(self.val)
        for child in self.children:
            child.depthFirstSearch(arr)
        return arr


root = Node("A")
root.addChild("B")
root.addChild("C")
root.addChild("D")
root.children[0].addChild("E")
root.children[0].addChild("F")
root.children[0].children[1].addChild("I")
root.children[0].children[1].addChild("J")
root.children[2].addChild("G")
root.children[2].addChild("H")
root.children[2].children[0].addChild("K")


print(root.depthFirstSearch([]))
