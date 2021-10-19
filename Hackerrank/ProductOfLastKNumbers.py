class ProductOfNumbers(object):
    def __init__(self):
        self.l = [1]

    def add(self, num):
        if not num:
            self.l = [1]
            return
        self.l.append(self.l[-1]*num)             

    def getProduct(self, k):
        if len(self.l) <= k:
            return 0
        return self.l[-1] // self.l[-1-k]


# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
