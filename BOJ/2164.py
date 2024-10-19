from collections import deque

N = int(input())

cardList = deque()
for i in range(1, N+1):
    cardList.append(i)

while True:
    if len(cardList) == 1:
        print(cardList[0])
        break
    cardList.popleft()
    cardList.append(cardList.popleft())
