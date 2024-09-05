N, X = map(int, input().split())

list = list(map(int, input().split()))
printList = []
for i in range(N):
    if list[i] < X:
        printList.append(list[i])

print(*printList, sep=' ')