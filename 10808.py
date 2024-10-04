alphabet = [0] * 26

word = list(input())

for i in word:
    alphabet[ord(i) - 97] += 1

print(*alphabet, sep=' ')

