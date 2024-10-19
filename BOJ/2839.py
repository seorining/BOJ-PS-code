def paintListFunc(list, n):
    count = -1
    for i in range(len(list)):
        for j in range(len(list[i])):
            num = 3*i + 5*j
            if num == n :
                count = i + j
                return count
            list[i][j] = num
    return count

def findList(list, n):
    check = False
    count = 0
    for i in list:
        if n in i:
            check = True
    return check

n = int(input())

paintCount = n // 3 + 1
paintList = [[i for i in range(paintCount)] for _ in range(paintCount)]

print(paintListFunc(paintList, n))
