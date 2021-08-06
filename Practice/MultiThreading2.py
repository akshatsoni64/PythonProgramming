from threading import Thread

def funcDemo(num):
    print("Hello", num)

if __name__=="__main__":
    t1 = Thread(target=funcDemo, args=(6,))
    t1.start()