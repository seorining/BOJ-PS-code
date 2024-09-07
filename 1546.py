input()
score = list(map(int, input().split()))

max = max(score)
sum = 0
for i in score:
    newScore = i / max * 100
    sum += newScore

print(sum / len(score))