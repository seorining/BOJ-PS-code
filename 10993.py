def paintStar(height, width, n):
    if n == 1:
        starBoard[height][width] = '*'
        return
    
    widthSize = 2 ** (n+1) - 3
    heightSize = 2 ** n - 1
    resize = 2**(n-1)-1
    
    if ~n&1:
        for i in range(widthSize):
            starBoard[height][width+i] = '*'
        for i in range(1, heightSize):
            starBoard[height+i][width + widthSize - 1 - i] = '*'
        for i in range(1, heightSize-1):
            starBoard[height+i][width+i] = '*'
        paintStar(height+resize , width+resize+1, n-1)
    else:
        for i in range(widthSize):
            starBoard[height][width+i] = '*'
        for i in range(1, heightSize):
            starBoard[height-i][width+widthSize-1-i] = '*'
        for i in range(1, heightSize -1):
            starBoard[height-i][width+i] = '*'
        paintStar(height-resize , width+resize+1, n-1)

##main##
n = int(input())
width = 2 ** (n+1) - 3
height = 2 ** n - 1

starBoard = [[' ' for _ in range(width)]for _ in range(height)]
            
if ~n&1:paintStar(0,0,n)
else : paintStar(height-1,0,n)

for _ in starBoard:
    print(''.join(_).rstrip(' '))