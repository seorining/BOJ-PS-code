def findCount(board):
    countW = 0
    countB = 0
    
    #"W"로 시작한다 가정
    for i in range(8):
        if i % 2 == 0:
            for j in range(8):
                if j % 2 == 0:
                    if board[i][j] == 'B':
                        countW += 1
                else:
                    if board[i][j] == 'W':
                        countW += 1
        else:
            for j in range(8):
                if j % 2 == 0:
                    if board[i][j] == 'W':
                        countW += 1
                else:
                    if board[i][j] == 'B':
                        countW += 1
    
    #"B"로 시작한다 가정
    for i in range(8):
        if i % 2 == 0:
            for j in range(8):
                if j % 2 == 0:
                    if board[i][j] == 'W':
                        countB += 1
                else:
                    if board[i][j] == 'B':
                        countB += 1
        else:
            for j in range(8):
                if j % 2 == 0:
                    if board[i][j] == 'B':
                        countB += 1
                else:
                    if board[i][j] == 'W':
                        countB += 1
    
    return countW if countW <= countB else countB

board = []
boardReSize = []
countColor = []

n, m = map(int, input().split())

for i in range(n):
    board.append(list(input()))

for i in range(n - 7):
    tempListX = board[i:i+8]
    for j in range(m - 7):
        tempListY = []
        for _ in range(8):
            tempListY.append(tempListX[_][j:j+8])
        boardReSize.append(tempListY)

for i in boardReSize:
    countColor.append(findCount(i))
    
print(min(countColor))