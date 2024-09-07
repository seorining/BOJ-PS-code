N = int(input())

roomCount = 1
sum = 1
for i in range(1, N+1):
    if sum >= N:
        print(roomCount)
        break
    sum = sum + 6 * roomCount
    roomCount += 1