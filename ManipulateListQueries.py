# get number of zeros in array
n, m = list(map(int, input("Enter N(Element Count), M(Queies Count):").split(" ")))
arr = []

# initialize list of n elements
for i in range(n):
    arr.append(0);
    
#  get queries
print("Enter Queries Now...")
for i in range(m):
    l = int(input("L: "))
    r = int(input("R: "))
    # mark the positions to increment according to queries given
    if l >= 0:
        arr[l] += 1
        
    if r < n-1:
        arr[r+1] -= 1

# calculate cummulative sum
marker = 0
for i in range(n):
    if arr[i] != 0:
        marker += arr[i]
    arr[i] = marker
    
    
# print final array
print(arr)
