from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

numList = deque()
stack = deque([0])
printList = []

for _ in range(n):
    numList.append(int(input()))
    
count = 1

for i in numList:
    if count > 100001:
        break
    
    check = stack.pop()
    stack.append(check)
    
    while check != i:
        if count > 100001:
            break
        stack.append(count)
        printList.append("+")
        count+=1
        check = stack.pop()
        stack.append(check)
    stack.pop()
    printList.append("-")


if len(stack) == 1:
    print(*printList, sep='\n')
else:
    print("NO")