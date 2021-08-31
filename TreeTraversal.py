class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data
        
class MainClass:
    def topView(self, root):
        self.leftView(root.left)
        print(root.data, end=" ")
        self.rightView(root.right)

    def leftView(self, root):
        if root != None:
            self.leftView(root.left)
            print(root.data, end=" ")
    
    def rightView(self, root):
        if root != None:
            print(root.data, end=" ")
            self.rightView(root.right)
    
    def height(self, root):
        leftHeight = 0
        rightHeight = 0
        
        if(root.left):
            leftHeight = self.height(root.left) + 1
        
        if(root.right):
            rightHeight = self.height(root.right) + 1
        
        if(leftHeight > rightHeight):
            return leftHeight
        else:
            return rightHeight
        
    def insertNode(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data < root.data:
                cur = self.insertNode(root.left, data)
                root.left = cur
            else:
                cur = self.insertNode(root.right, data)
                root.right = cur
        return root
        
    def levelOrder(self, root):
        nodes_to_search = list()
        nodes_traversed = list()
        nodes_to_search.append(root)
        while len(nodes_to_search) > 0:
            node = nodes_to_search.pop(0)
            if node.left:
                nodes_to_search.append(node.left)  
            if node.right:
                nodes_to_search.append(node.right)
            nodes_traversed.append(node.data)
        print(*nodes_traversed)
        
    def inOrder(self, root):
        if root != None:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)

        return
        
    def preOrder(self, root):
        if root != None:
            print(root.data, end=" ")
            self.inOrder(root.left)
            self.inOrder(root.right)

        return
        
    def postOrder(self, root):
        if root != None:
            self.inOrder(root.left)
            self.inOrder(root.right)
            print(root.data, end=" ")

        return

# ip = input("Input Nodes: ")
# ip = "37 23 108 59 86 64 94 14 105 17 111 65 55 31 79 97 78 25 50 22 66 46 104 98 81 90 68 40 103 77 74 18 69 82 41 4 48 83 67 6 2 95 54 100 99 84 34 88 27 72 32 62 9 56 109 115 33 15 91 29 85 114 112 20 26 30 93 96 87 42 38 60 7 73 35 12 10 57 80 13 52 44 16 70 8 39 107 106 63 24 92 45 75 116 5 61 49 101 71 11 53 43 102 110 1 58 36 28 76 47 113 21 89 51 19 3"
# vals = list(map(int, ip.split(" ")))
vals = [6, 3, 5, 4, 7, 2, 1]
obj = MainClass()
root = None

for val in vals:
    root = obj.insertNode(root, val)
print("Tree Top View: ", end="")
obj.topView(root)
print("\n\nLevel-order Traversal: ", end="")
obj.levelOrder(root)
print("\nIn-order Traversal: ", end="")
obj.inOrder(root)
print("\n\nPre-order Traversal: ", end="")
obj.preOrder(root)
print("\n\nPost-order Traversal: ", end="")
obj.postOrder(root)
