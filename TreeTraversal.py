class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data
        
class MainClass:
    tr = []
    def topView(self, root):
        if root.left:
            self.leftView(root)
            t = reversed(self.tr)
            print(*t, end=" ")
        
        if root.right:
            self.rightView(root)

    def leftView(self, root):
        if root != None:
            self.tr.append(root.data)
            self.leftView(root.left)
    
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

# vals = list(map(int, input("Input Nodes: ").split(" ")))
vals = [6, 3, 5, 4, 7, 2, 1]
obj = MainClass()
root = None

for val in vals:
    root = obj.insertNode(root, val)
print("Level-order Traversal: ", end="")
obj.levelOrder(root)
print("\nIn-order Traversal: ", end="")
obj.inOrder(root)
print("\n\nPre-order Traversal: ", end="")
obj.preOrder(root)
print("\n\nPost-order Traversal: ", end="")
obj.postOrder(root)
