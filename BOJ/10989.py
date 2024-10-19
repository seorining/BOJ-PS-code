import sys
n = int(sys.stdin.readline())
numCount = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    numCount[num] += 1
    
for i in range (10001):
    if numCount[i] != 0:
        for j in range(numCount[i]):
            print(i)