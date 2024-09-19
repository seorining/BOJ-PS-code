import math

n, m = map(int, input().split())
primeList = [True for i in range(m+1)]
primeList[1] = False

for i in range(2, int(math.sqrt(m)) + 1):
    if primeList[i] == True:
        j = 2
        while i*j <= m:
            primeList[i * j] = False
            j += 1
            
for i in range(n, m+1):
    if primeList[i] == True:
        print(i)