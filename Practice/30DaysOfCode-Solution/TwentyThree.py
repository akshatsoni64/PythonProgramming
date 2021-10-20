class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data
        
class MainClass:
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
        print(str(data)+" Inserted\n")
        return root
        
    def levelOrder(self,root):
        nodes_to_search = list();
        nodes_traversed = ''
        nodes_to_search.append(root)
        while len(nodes_to_search) > 0:
            node = nodes_to_search.pop(0)
            if node.left:
                nodes_to_search.append(node.left)  
            if node.right:
                nodes_to_search.append(node.right)
            nodes_traversed += str(node.data) + ' '
        print(nodes_traversed)

vals = list(map(int, input("Input Nodes: ").split(" ")))
obj = MainClass()
root = None

for val in vals:
    print("\nInserting "+str(val))
    root = obj.insertNode(root, val)
print("Level-order Traversal: ", end="")
obj.levelOrder(root)
