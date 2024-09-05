T = int(input())

printWord = []

for _ in range(T):
    word = input()
    printWord.append([word[0],word[-1]])

for _ in printWord:
    print(*_, sep='')