class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        p1 = headA
        p2 = headB
        
        while p1 is not p2:
            p1 = headB if p1 is None else p1.next
            p2 = headA if p2 is None else p2.next
        
        return p1
    
    def hasCycle(self, head):
        while head:
            if head.val == None:
                return True
            head.val = None
            head = head.next
        return False
        
    def middleNode(self, head):
        sp = fp = head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        
        return sp
        
    def swapPairs(self, head):
        temp = head
        
        while temp and temp.next:
            temp.data, temp.next.data = temp.next.data, temp.data
        
            temp = temp.next.next
        
        return head
        
        
    def getDecimalValue(self, head):
        st = []
        while head:
            st.append(head.val)
            head = head.next
        st.reverse()
        intt = 0
        for i in range(len(st)):
            intt += (st[i]*(2**i))
        return intt


    def compare_lists(llist1, llist2):
        res = 0
        while llist1 and llist2 and llist1.data == llist2.data:
            llist1 = llist1.next
            llist2 = llist2.next
        return 1 if not llist1 and not llist2 else 0


    def reverse(llist):
        curr = llist
        previous = None
        following = curr.next
        while curr:
            curr.next = previous
            previous = curr
            curr = following
            if following:
                following = following.next
        return previous

        
    def reversePrint(llist):
        st = []
        while(llist.next != None):
            st.insert(0, llist.data)
            llist = llist.next
        print(llist.data, *st, sep="\n")
        

    def removeDuplicates(self, head):
        if head is None:
            return
        
        curr = head
        while curr.next != None:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
            
        return head
        
    
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
        
    
    def deleteNodeFromEnd(self, head, n):
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
    
    head = l.removeDuplicates(head)
    l.printList(head)
    
    # n = int(input("Enter Number Position to delete from backside: "))
    # head = l.deleteNodeFromEnd(head, n)
    
    # l.printList(head)
