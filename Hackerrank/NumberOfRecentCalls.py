class RecentCounter:
    def __init__(self):
        self.queue = []
        

    def ping(self, t: int) -> int:
        while len(self.queue) and t-3000 > self.queue[0]:
            self.queue.pop(0)
        self.queue.append(t)
        return len(self.queue)


obj = RecentCounter()
l = [1, 100, 3001, 3002]
print([None]+[obj.ping(v) for v in l])
