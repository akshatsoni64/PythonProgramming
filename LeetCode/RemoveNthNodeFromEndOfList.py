class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertNode(self, head, data):
        if head != None:
            curr = head
            while curr.next != None:
                curr = curr.next
            curr.next = LinkedListNode(data)
            curr.next.next = None
        else:
            head = LinkedListNode(data)
            head.next = None
        
        return head
        
    def printList(self, head):
        print("\nList:")
        if head != None:
            while head != None:
                print(head.data)
                head = head.next
        else:
            print("List is empty!")
        
    def deleteNode(self, head, n):
        # Get length of linkedlist
        temp = head
        numNodes = 0
        while temp is not None:
            temp = temp.next
            numNodes += 1
        
        # Get element position
        k = numNodes - n
        print("Position of element:", k)
        
        prev = None
        ptr = head
        # Traverse linkedlist till the position-1
        while k != 0:
            prev = ptr
            ptr = ptr.next
            k -= 1
        
        # If first Element is to be removed
        if prev is None:
            return head.next
        # Remove node from the linkedlist
        else:
            prev.next = ptr.next
            ptr.next = None
            return head
            
if __name__ == "__main__":
    l = LinkedList()
    head = None
    data = list(map(int, input("Enter LinkedList Data (space separated): ").split(" ")))
    for val in data:
        head = l.insertNode(head, val)
    
    l.printList(head)
    
    n = int(input("Enter Number Position to delete from backside: "))
    head = l.deleteNode(head, n)
    
    l.printList(head)
