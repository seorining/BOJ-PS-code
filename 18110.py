from collections import deque
import sys
input = sys.stdin.readline

def realRound(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else: return int(n)

n = int(input())
difficultList = [int(input()) for _ in range(n)]
difficultList.sort()
difficultList = deque(difficultList)

cut = int(realRound(n / 100 * 15))

for i in range(cut):
    difficultList.pop()
    difficultList.popleft()

sum = 0
for i in difficultList:
    sum += i

try :
    print(realRound(sum / len(difficultList)))
except:
    print(0)