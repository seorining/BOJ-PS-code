def sumAll(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

T = int(input())

score = []

for i in range(T):
    result = list(input())
    sum = 0
    count = 0
    for i in result:
        if i == 'O':
            count += 1
        else:
            sum += sumAll(count)
            count = 0
    sum += sumAll(count)
    score.append(sum)
    
for _ in score:
    print(_)