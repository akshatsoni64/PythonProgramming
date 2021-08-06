'''

AIM - Find unique elements from array after m numbers of deletion

Testcases:

Input: arr[] = {2, 2, 1, 3, 3, 3} m = 3
Output: 1
Explanation:
Remove 1 and both 2’s.
So, only 3 will be left, hence distinct number of element is 1.

Input: arr[] = {2, 4, 1, 5, 3, 5, 1, 3} m = 2
Output: 3
Explanation:
Remove 2 and 4 completely. 
So, remaining 1, 3 and 5 i.e. 3 elements.


'''

arr= [2, 4, 1, 5, 3, 5, 1, 3]
m = 2
d = {}

for val in arr[m:]:
    if val in d.keys():
        d[val] += 1
    else:
        d[val] = 1
        
print(len(d.keys()))
