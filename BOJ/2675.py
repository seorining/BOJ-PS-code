T = int(input())

printWord = []

for _ in range(T):
    num, word = input().split()
    makeWord = []
    for j in word:
        makeWord.append([int(num) * j])
    printWord.append(makeWord)

for _ in printWord:
    for i in _:
        print(*i, sep='', end='')
    print()