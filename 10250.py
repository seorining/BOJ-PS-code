T = int(input())

roomNum = []

for _ in range(T):
    room = list(map(int, input().split()))
    height = room[2] % room[0]
    width = room[2] // room[0] + 1
    if height == 0 : 
        height=room[0]
        width -= 1
    roomNum.append('{:}{:>02}'.format(height, width))

for _ in roomNum:
    print(*_, sep='')