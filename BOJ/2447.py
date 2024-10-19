x = int(input())

board = [[' ' for row in range(x)] for col in range(x)]

def printBoard():
    for i in board:
        for j in i:
            print(j, end="")
        print()

def drawStar(width, length, num):
    if num == 3:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                else:
                    board[width+i][length+j] = '*'
        return
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                drawStar(width+i*int(num/3), length+ j*int(num/3), int(num/3))
                
    

drawStar(0, 0, x)
        
printBoard()