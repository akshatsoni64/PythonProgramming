class MyCircularDeque:

    def __init__(self, k: int):
        self.q = []
        self.sz = k
        

    def insertFront(self, value: int) -> bool:
        if len(self.q) < self.sz:
            self.q.insert(0, value)
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.q) < self.sz:
            self.q.append(value)
            return True
        return False
        

    def deleteFront(self) -> bool:
        if self.q:
            self.q.pop(0)
            return True
        return False
        

    def deleteLast(self) -> bool:
        if self.q:
            self.q.pop()
            return True
        return False
        

    def getFront(self) -> int:
        return self.q[0] if self.q else -1
        

    def getRear(self) -> int:
        return self.q[-1] if self.q else -1
        

    def isEmpty(self) -> bool:
        return not bool(self.q)
        

    def isFull(self) -> bool:
        return len(self.q) == self.sz
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
