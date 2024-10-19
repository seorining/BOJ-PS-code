word = list(input())

for _ in word:
    print(_.lower(), end='') if _.isupper() else print(_.upper(), end='')