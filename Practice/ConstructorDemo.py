class ConstructorDemo:
    def __init__(self):
        print("Object Initialized")

    def __del__(self):
        print("Object Deleted")


if __name__ == "__main__":
    ob = ConstructorDemo()
    print("Exit")
