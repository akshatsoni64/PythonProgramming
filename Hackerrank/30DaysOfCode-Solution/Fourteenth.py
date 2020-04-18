class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        diffList = []
        for i in range(0, len(self.__elements)):
            for j in range(i, len(self.__elements)):
                diffList.append(abs((self.__elements[i]) - (self.__elements[j])))
        diffList.sort(reverse=True)
        self.maximumDifference = diffList[0]

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)