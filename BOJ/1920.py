N = int(input())
A = [i for i in map(int, input().split())]
int(input())
findList = [i for i in map(int, input().split())]

A.sort()

for i in findList:
    first, end = 0, N - 1
    isFind = False
    
    while first <= end:
        mid = (first + end) // 2
        if i == A[mid]:
            isFind = True
            print(1)
            break
        elif i < A[mid]:
            end = mid - 1
        else:
            first = mid + 1
    if not isFind:
        print(0)