import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

def findbaechu(i, j):
    for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
        if x<0 or y<0 or x>=n or y>=m:
            continue
        if flied[x][y] == 1:
            flied[x][y] = 0
            findbaechu(x,y)

for _ in range(t):
    m, n, k = map(int, input().split())
    count = 0
    flied = [[0 for i in range(m)] for j in range(n)]
    
    for i in range(k):
        x, y = map(int, input().split())
        flied[y][x] = 1
        
    for i in range(len(flied)):
        for j in range(len(flied[i])):
            if flied[i][j] == 1:
                flied[i][j] = 0
                findbaechu(i, j)
                count += 1
                
    print(count)