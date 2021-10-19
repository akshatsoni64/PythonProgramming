class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.sz = k


    def enQueue(self, value: int) -> bool:
        if len(self.q) < self.sz:
            self.q.append(value)
            return True
        return False
        
        

    def deQueue(self) -> bool:
        if len(self.q) > 0:
            self.q.pop(0)
            return True
        return False
        

    def Front(self) -> int:
        return self.q[0] if self.q else -1
        

    def Rear(self) -> int:
        return self.q[-1] if self.q else -1
        

    def isEmpty(self) -> bool:
        return not bool(self.q)
        

    def isFull(self) -> bool:
        return len(self.q) == self.sz
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
