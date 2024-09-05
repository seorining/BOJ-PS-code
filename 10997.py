n= int(input())

pos = 2*n - 1

def firstStar(i):
    return ['*' if ~j&1 else ' ' for j in range(i)]
    
def firstBlank(i):
    return ['*' if j&1 else ' ' for j in range(i)]

def printStar(i):
    return ['*' for j in range(i)]

def printBlank(i):
    return [' ' for j in range(i)]

def recursionStar(x, n):
    if n == 1:
        board[0][x]='*'
        return
    for i in range(2*n-1):
        board[i][x] = '*'
    for i in range(4*n-3):
        board[2*n-2][x+i] = '*'
    for i in range(2*n-1):
        board[2*n-2-i][4*n-4+x] = '*'
    return recursionStar(x+2, n-1)

for i in range(pos+1):
    if n == 1:
        break
    if i == 0:
        print(*(printStar(4*n-3)), sep='')
        continue
    if i == 1:
        print("*")
        continue
    if ~i&1:
        print(*(firstStar(i) + printStar(4*(n-i//2) - 1) + firstBlank(i-2)), sep='')
    else:
        print(*(firstStar(i) + printBlank(4*(n-i//2)-3) + firstStar(i-2)), sep='')
        
board = [[' 'for _ in range(4*n-3)] for _ in range(pos)]
recursionStar(0, n)

for _ in board:
    print(*_, sep='')