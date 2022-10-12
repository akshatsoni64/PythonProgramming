class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

if __name__ == "__main__":
    n = 7
    root = Node('1')
    one = Node('4')
    two = Node("")
    three = Node('7')
    four = Node("")
    five = Node('2')
    six = Node('8')
    
    root.next = one
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six
    six.next = None
    
    node = root
    value = ""
    flag = True
    while(node is not None):
        if node.val:
            value += node.val
        else:
            flag = bool(int(value)%n == 0)
            value = ""
        node = node.next
    
    print(flag)
