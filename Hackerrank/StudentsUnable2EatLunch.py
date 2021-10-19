def countStudents(students, sandwiches):
    flag = 0
    n = len(sandwiches)
    while sandwiches and flag <= n:
        if students[0] == sandwiches[0]:
            sandwiches.pop(0)
            n -= 1
            students.pop(0)
            flag = 0
        else:
            students.append(students.pop(0))
            flag += 1
    return n

print(
    countStudents(
        [1,1,1,0,0,1],
        [1,0,0,0,1,1]
    )
)
