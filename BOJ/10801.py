aCard = list(map(int, input().split()))
bCard = list(map(int, input().split()))

win = 0

for i in range(len(aCard)):
    if aCard[i] > bCard[i]:
        win += 1
    elif aCard[i] < bCard[i]:
        win -= 1
        
if win > 0:
    print("A")
elif win < 0:
    print("B")
else:
    print("D")