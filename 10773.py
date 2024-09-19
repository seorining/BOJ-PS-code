from collections import deque

numberList = []
k = int(input())
stack = deque()

for i in range(k):
    numberList.append(int(input()))

for i in numberList:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)
sum = 0
for i in stack:
    sum += i
print(sum)