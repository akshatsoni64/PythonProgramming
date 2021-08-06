from threading  import Thread

class Thread1(Thread):
    def __init__(self, num):
        super(Thread1, self).__init__()
        self.num = num

    def run(self):
        print("Cube of 6: {0}".format(self.num * self.num * self.num))

class Thread2(Thread):
    def __init__(self, num):
        super(Thread2, self).__init__()
        self.num = num

    def run(self):
        print("Square of 6: {0}".format(self.num * self.num))


if __name__ == "__main__": 
    t1 = Thread1(6)
    t2 = Thread2(6)
    t1.start()
    t2.start()