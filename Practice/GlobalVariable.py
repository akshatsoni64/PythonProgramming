x = 20


def func():
    x = 10
    print("Local: " + str(x))


func()
print("Global: " + str(x))
