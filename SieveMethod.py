no = int(input("Enter Range: "))
lst = [i for i in range(2, no+1)]
lst_rem = []


for i in lst:
    p = i
    j = i
    k = 0
    l = 0
    while l >= lst[-1]:
        l = l + (j*(j+k))
        lst_rem.append(j*(j+k))
        ++k

#for a in lst_rem:
    #lst.remove(a)
print(lst)
print(lst_rem)
