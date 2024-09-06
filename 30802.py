N = int(input())
people = list(map(int, input().split()))
T, P = map(int, input().split())

tshirtCount = 0

for i in people:
    if i == 0:
        continue
    elif i <= T:
        tshirtCount += 1
    elif i % T == 0:
        tshirtCount += i // T
    else:
        tshirtCount += i // T + 1
        

print(tshirtCount)
print(N // P, N % P)