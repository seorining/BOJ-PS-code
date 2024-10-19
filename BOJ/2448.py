import math

def paintStar(height, width, n):
    if n == 1:
        board[height][width] = '*'
        board[height+1][width-1] = '*'
        board[height+1][width+1] = '*'
        for i in range(5):
            board[height+2][width-2+i] = '*'
        return
    
    resize = 3*int(2**(n-2))
    paintStar(height, width, n-1)
    paintStar(height+resize, width-resize, n-1)
    paintStar(height+resize, width+resize, n-1)


n = int(input())
n = int(math.log2(n // 3)) + 1

width = 6*(2**(n-1)) - 1
height = 3*(2**(n-1))

board = [[' ' for _ in range(width)] for _ in range(height)]
paintStar(0, int(6*(2**(n-2))-1), n)

for _ in board:
    print(''.join(_))